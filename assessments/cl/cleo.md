---
harness_id: cleo
project_name: CLEO
repository: https://github.com/kryptobaseddev/cleo
review_ref: 84af0f9becd7b0f1279587cf3c85c793b76a5686
reviewed_at: 2026-10-27
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: included
autonomy_s1: A
autonomy_s2: C
autonomy_s3: P
autonomy_s3_star: —
autonomy_s4: C(P)
autonomy_s5: —
---

# CLEO

## Review boundary

- System in focus: an installed CLEO project-scoped task/orchestration runtime, including configured provider-backed spawned workers, resource/claim control and explicitly opt-in sentient daemon Tier-1/Tier-2 modes, not its repository maintenance team.
- Purpose and identity: preserve multi-agent task/session continuity, coordinate bounded work across coding-agent providers, check completion against evidence and offer a controlled path from detected project changes to later work.
- Relevant environment: local source trees and Git worktrees, external Claude Code/OpenCode/Codex/Gemini/etc. providers, task dependencies, machine memory pressure, test commands, code/symbol graph and long-lived project observations.
- Standard-distribution boundary: published CLI/Core/OS packages, task/session SQLite stores, orchestration spawn adapters, per-agent identity/claims, machine admission ledger, opt-in sentient daemon, memory/NEXUS scanners and user owner commands. An opt-in in-process Pi model loop is a separate shipped mode and defaults off; external provider cognition is not authored in CLEO.
- Credited operating / distribution surfaces: `packages/core/src/orchestrate/`, `spawn/`, `task-work/claims.ts`, `tasks/tool-semaphore.ts`, `resources/admission-ledger.ts`, `sentient/tick.ts`, `sentient/propose-tick.ts`, `sentient/dream-cycle.ts`, `llm/pi/`, and actual CLI/OS entry points.
- Adjacent first-party surfaces excluded from ownership: repository `docs/plans/`, contributor/release governance, test injection fixtures and benchmark stubs, template CANT agent names and `@cleocode/skills` text without runtime invocation, third-party agent's independent hosting organization.
- First-party operating / deployment modes considered: normal `cleo orchestrate spawn` with configured provider and separate child session, `cleo agent work --execute`, project-scoped sentient Tier-1 daemon, opt-in Tier-2 future-task ingestion/autopromotion, manual proposal acceptance, machine-wide evidence-tool admission, optional in-process Pi runner and owner kill/resume.
- Recursion level: one CLEO-controlled project/task operation with active spawned S1 agents and local current-control owner; machine-wide tool admission is shared infrastructure observed as an inter-worker relation, not proof that every user project forms a single metaproject viable system.
- Reviewed revision: `84af0f9becd7b0f1279587cf3c85c793b76a5686`.
- Observation date: 2026-10-27.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

CLEO is a TypeScript/Rust monorepo with an installed CLI, Core task/session/orchestration SDK, protocol adapters, CANT agent definitions, code/NEXUS intelligence, BRAIN memory and a separate optional sentient daemon. A normal spawn binds a configured external model-driven coding CLI to an isolated per-agent task/session and, where requested, worktree. Tasks have dependencies and claims; claims refuse competing unrelated holders. Evidence tools from different worktree agents are admitted through a machine-wide memory-based budget/FIFO ledger, preventing concurrent heavy test/build execution from overwhelming the host. The daemon's default Tier-1 tick chooses ready tasks by dependency order, spawns external agents, independently re-runs canonical tests/checks after worker success reports and backs off or self-pauses on repeated failure. Owner kill/resume and attestation for post-revert resume are first-party controls. Separate Tier-2, disabled by default, mines BRAIN/NEXUS/test-gate disturbances into future-task proposals; a threshold and readiness grill can autonomously promote these to the Tier-1 pending queue, while an owner can manually accept proposals. Optional Pi embedding provides a real model/tool loop behind a default-off feature flag. Most orchestration and queue logic remains deterministic; independent semantic judgments by the external worker model are not attributed to the CLEO TypeScript host.

Primary sources: [README product/deployment boundary](https://github.com/kryptobaseddev/cleo/blob/84af0f9becd7b0f1279587cf3c85c793b76a5686/README.md), [spawn implementation](https://github.com/kryptobaseddev/cleo/blob/84af0f9becd7b0f1279587cf3c85c793b76a5686/packages/core/src/orchestrate/spawn-ops.ts), [machine admission](https://github.com/kryptobaseddev/cleo/blob/84af0f9becd7b0f1279587cf3c85c793b76a5686/packages/core/src/tasks/tool-semaphore.ts), [Tier-1 tick](https://github.com/kryptobaseddev/cleo/blob/84af0f9becd7b0f1279587cf3c85c793b76a5686/packages/core/src/sentient/tick.ts), [Tier-2 proposals](https://github.com/kryptobaseddev/cleo/blob/84af0f9becd7b0f1279587cf3c85c793b76a5686/packages/core/src/sentient/propose-tick.ts).

## Operational model

Model-driven tools and task actions belong to configured child agents, while CLEO supplies launch/identity, task claims, real execution environment and re-verification. Agent-selected work and CLEO's deterministic admission are distinguishable. S2 has a first-party *constructor* that attenuates a specific inter-agent execution conflict through shared resource admission, not a human-free autonomous model coordinating peers. S3 includes an explicitly reachable operator-run current-control mode: the owner can stop/restart the project daemon and intervene in stuck/revert conditions. S4 has a separate supported future-candidate constructor (default-off Tier-2, automatic scoring/readiness and Tier-1 handoff) and a parent manual acceptance mode. Automated evidence checks do not automatically become S3*.

## S1 — Operations

- State: A
- Function: deliver actual coding/task artifacts through configured model-backed subagents, optional Pi in-process agent/tool loop, and iterative tool feedback.
- Disturbance / variety regulated: code changes, failing tools/tests, new task requirements and external provider/model behavior.
- Decisive decision or feedback right: choose contextual next work/tool action, revise in response to execution output and report task result.
- Decision owner: launched external provider-backed CLI agents in normal spawn paths; optionally in-process Pi/model agent under explicit flag, not the deterministic Tier-1 task picker.
- Supporting / enforcement mechanisms: adapter-registry eligibility, `orchestrate.spawn`, distinct child session/identity, task/worktree claims, injected tools, Pi guarded execution environment and result receipts.
- Closure path: CLI/agent receives task, executes tools against scoped workspace, consumes results, and returns evidence/output via task and spawn receipt to CLEO; further task turns may react to feedback.
- Boundary reachability: supported `cleo orchestrate spawn` and `cleo agent work --execute` CLI modes call these adapters. The optional Pi runner is a separate first-party installed daemon path, not test code.
- Why this is / is not agent-owned: dynamic tool/task decisions are made by invoked coding-agent/model cognition; CLEO's task DB and scheduling alone do not decide how to implement a task.
- Evidence: [provider-backed normal spawn](https://github.com/kryptobaseddev/cleo/blob/84af0f9becd7b0f1279587cf3c85c793b76a5686/packages/core/src/orchestrate/spawn-ops.ts#L760-L925), [per-agent session identity](https://github.com/kryptobaseddev/cleo/blob/84af0f9becd7b0f1279587cf3c85c793b76a5686/packages/core/src/spawn/agent-identity.ts#L185-L254), [optional in-process Pi](https://github.com/kryptobaseddev/cleo/blob/84af0f9becd7b0f1279587cf3c85c793b76a5686/packages/core/src/llm/pi/index.ts), [work-loop](https://github.com/kryptobaseddev/cleo/blob/84af0f9becd7b0f1279587cf3c85c793b76a5686/packages/core/src/agents/work-loop.ts).
- Basis: explicit and structural.
- Confidence: high.
- Caveats: external providers require configuration and credentials. Pi is explicitly default off. No live external LLM/agent run performed.

## S2 — Coordination

- State: C
- Function: prevent concurrently working S1 agents from oversubscribing machine resources or claiming incompatible ownership of the same task.
- Disturbance / variety regulated: multiple worktree agents independently run heavy tests and builds against distinct HEADs; per-key caches cannot deduplicate this, causing CPU/memory contention; unrelated agents may also race on one task.
- Decisive decision or feedback right: acquire/withhold a shared resource grant and acquire/refuse a task lease before entering agent work; an invoking agent can wait, retry or choose another task based on refusal.
- Decision owner: deterministic first-party admission/claim constructor, not a proven autonomous multi-agent negotiation owner. The task agent initiates work that requires the grant and receives its result.
- Supporting / enforcement mechanisms: machine-wide `resources/admission-ledger.ts` with FIFO bytes budget and pressure gate, inherited `CLEO_ADMISSION` grant, task claim chokepoint and child-specific identity/worktree mapping.
- Closure path: parallel test/tool requests compete for the same shared ledger and are queued/admitted within measured pressure; agents execute only after admission, avoiding cross-agent resource blow-up. A second task claimant is rejected, preserving one effective owner and returning an actionable failure.
- Boundary reachability: normal `cleo verify`/`cleo run`/agent evidence tool paths take the shared ledger; normal spawned agents obtain task leases in the production spawn path rather than a template alone.
- Why this is / is not agent-owned: the interference-specific relation is shipped, but the deciding capacity policy and FIFO are deterministic. Therefore `C`, not `A`; no external test harness or model-led arbitration is invented.
- Distinct S1 units: concurrently spawned model-backed agents, often in separate Git worktrees.
- Inter-S1 disturbance: simultaneous heavy execution on different cache keys exhausts host resources; duplicate task claimants risk inconsistent writes.
- Attenuating coordination relation: one machine-wide admission queue/budget and trusted task-lease family prevent uncontrolled concurrency at the contested resources.
- Feedback into subsequent S1 behaviour: admission or claim rejection returns failure/wait information to the invoking run; admitted tools operate under inherited grant and subsequent agent work observes the bounded result.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: resource evidence documents a precise *between-agent* conflict beyond DAG ordering, and enforcement spans independent worktrees/processes rather than merely collecting statuses.
- Evidence: [resource collision analysis and admission](https://github.com/kryptobaseddev/cleo/blob/84af0f9becd7b0f1279587cf3c85c793b76a5686/packages/core/src/tasks/tool-semaphore.ts#L1-L51), [shared ledger](https://github.com/kryptobaseddev/cleo/blob/84af0f9becd7b0f1279587cf3c85c793b76a5686/packages/core/src/resources/admission-ledger.ts), [claim competition](https://github.com/kryptobaseddev/cleo/blob/84af0f9becd7b0f1279587cf3c85c793b76a5686/packages/core/src/task-work/claims.ts#L260-L319).
- Basis: explicit and structural.
- Confidence: medium-high.
- Caveats: task claim family may legitimately reuse a lease; no S2 agent that plans optimal resource allocation is claimed. The machine-wide ledger spans local operations but is not evidence of cross-project organizational S3.

## S3 — Inside-and-now control

- State: P
- Function: the legitimate project operator can govern current autonomous daemon commitments, global halt, restart and sensitive recovery.
- Disturbance / variety regulated: runaway or repeatedly stuck workers, unsafe continuation after revert and competing unattended operations.
- Decisive decision or feedback right: install/enable/scope daemon, activate kill-switch/stop, and deliberately resume after pause or owner-attested revert recovery.
- Decision owner: local project owner/operator using shipped CLEO commands; deterministic daemon admission, self-pause and watchdog are supporting enforcement.
- Supporting / enforcement mechanisms: daemon current task/state/stats, user kill/resume API, active-task recording, dependency picking, retry/backoff, stuck-rate kill-switch and owner attestation.
- Closure path: owner changes daemon control state, all ticks check it before pick/spawn/record, pending operations stop or later resume, and updated status is reported through the CLI; a revert pause cannot silently bypass required owner decision.
- Boundary reachability: `cleo sentient stop/resume/status` and owner-attested recovery are packaged supported owner commands, and the sentient daemon checks the same state in real tick execution.
- Why this is / is not agent-owned: task scheduling and self-pause thresholds are deterministic and do not imply a model-owned whole-project current-control policy; the operator owns the discretionary intervention.
- Whole-system current view: daemon stats, active task, stuck/failure history and kill/revert status across this project's unattended runs.
- Current-control decision scope: project daemon's permission to continue launching/receiving child work, not just one child's next tool call.
- Evidence: [daemon owner kill/resume](https://github.com/kryptobaseddev/cleo/blob/84af0f9becd7b0f1279587cf3c85c793b76a5686/packages/core/src/sentient/daemon.ts#L1075-L1175), [kill-switch checkpoints and self-pause](https://github.com/kryptobaseddev/cleo/blob/84af0f9becd7b0f1279587cf3c85c793b76a5686/packages/core/src/sentient/tick.ts#L795-L1080), [sentient CLI](https://github.com/kryptobaseddev/cleo/blob/84af0f9becd7b0f1279587cf3c85c793b76a5686/packages/cleo/src/cli/commands/sentient.ts).
- Basis: explicit and structural.
- Confidence: medium-high.
- Caveats: P applies to installed opt-in sentient daemon/project operating mode; normal stateless CLI sessions alone do not inherit a full live team supervisor. Daemon automated retries are not model-owned S3.

## S3* — Complementary audit

- State: —
- Function: no independently governed, nonroutine complementary audit owner established beyond mandatory worker-acceptance re-verification.
- Disturbance / variety regulated: a worker falsely reports success, files or test evidence differ from its claim.
- Decisive decision or feedback right: the orchestrator deterministically reruns affected/full tests and checks Git/file/evidence before accepting a worker's normal completion receipt.
- Decision owner: routine first-party verification gate, not a separately constituted agent auditor; its checks are enforcement rather than autonomous S3* judgment.
- Supporting / enforcement mechanisms: `reVerifyWorkerReport`, test runner and Git status from actual worktree, mismatch JSONL and retry/backoff after rejection.
- Closure path: false-success claims are downgraded to failed work and re-enter ordinary retry flow, but this mandatory same-workflow acceptance check does not create independent sporadic metasystem access/owner.
- Why this is / is not agent-owned: a worker cannot simply mark itself complete, yet deterministic routine verification is not by itself complementary S3* ownership under Profile 0.2.4.
- Evidence: [worker evidence gate](https://github.com/kryptobaseddev/cleo/blob/84af0f9becd7b0f1279587cf3c85c793b76a5686/packages/core/src/orchestrate/worker-verify.ts#L1-L126), [admission into Tier-1 acceptance](https://github.com/kryptobaseddev/cleo/blob/84af0f9becd7b0f1279587cf3c85c793b76a5686/packages/core/src/sentient/tick.ts#L880-L1035).
- Basis: explicit and structural.
- Confidence: medium-high.
- Caveats: this is unusually evidence-rich routine verification, but no alternative auditor-led, nonroutine reality-probe path is credited as closed S3*.

### Absence scope

- Surfaces inspected: worker re-verification, test/cache/admission tools, audit mismatch logs, Tier-1 receipt/state flow, owner controls and contributor diagnostics.
- Plausible first-party paths checked: actual Git/test checks, worker reported-evidence comparison, background skill review, and deterministic project audit logs.
- Why no material first-party path remains: these are obligatory worker completion controls or developer/learning functions, not a distinct complementary independent audit decision path with returned metasystem control at the declared project boundary.

## S4 — Outside-and-then intelligence

- State: C(P)
- Function: surface new prospective work arising from project/environment evidence and feed vetted future capability/task adaptations into the Tier-1 execution queue.
- Disturbance / variety regulated: emerging BRAIN observations, NEXUS code-dependency drift and failing test/gate evidence indicate future repair opportunities outside the immediate selected task.
- Decisive decision or feedback right: first-party opt-in Tier-2 ingesters generate structured future proposals and an automatic weight/readiness gate can promote acceptable ones; separately, the project owner can choose to accept a proposal that remains pending review.
- Decision owner: `C` is deterministic detection/promotion constructor with no model-owned autonomous strategic selection proven; `P` is the operator deciding manual proposal acceptance. Neither is claimed as full agent-owned S4 foresight.
- Supporting / enforcement mechanisms: BRAIN/NEXUS/test ingesters, dedup fingerprints, daily rate limit, `tier2Enabled` guard, proposal `weight` and readiness grill, `proposed→pending` handoff, Tier-1 task picker and owner `cleo sentient propose accept`.
- Closure path: source observations from project environment become explicit future-task candidates; enabled Tier-2 stores them, a gated scan can promote eligible ones to pending, and subsequent Tier-1 ticks select/spawn actual S1 work. In parent mode an owner approves a proposed task before that same S1 handoff.
- Boundary reachability: Tier-2 proposal timer/CLI/guard and auto-promotion are shipped in the sentient daemon but default off until owner explicitly enables. The separate manual proposal acceptance is a packaged CLI operation. Only an enabled daemon with working external agents can close through task execution.
- Why this is / is not agent-owned: the supported constructive loop connects exterior evidence and later work, but title templating and threshold/grill selection are deterministic, not evidence of strategic model-authored foresight.
- External distinction: ingesters inspect code/NEXUS changes, test failures and persisted project observations beyond the present agent's task/own log counter.
- Future / prospective distinction: Tier-2 creates an additional task not in the current workload and defers execution into later Tier-1 ticks, separate from ordinary present-task repair.
- Adaptation option generated: a deduplicated, weighted future task proposal for a detected code/test/knowledge disturbance.
- Path back into current capability / S3: gated promotion or owner acceptance turns the proposed future option into a pending task subject to the existing project queue, owner kill-switch and normal spawned-agent execution.

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (`C`) | deterministic Tier-2 proposal/weight/readiness constructor | owner-enabled Tier-2 scans BRAIN/NEXUS/test environment | scored readiness promotion to Tier-1 pending tasks, later spawned into operational work | `sentient/propose-tick.ts`, `sentient/tick.ts` |
| Parent (`P`) | legitimate project owner | owner reviews/accepts a previously generated proposal | CLI `sentient propose accept` admits it to future Tier-1 work | `cleo/src/cli/commands/sentient.ts` |

- Evidence: [Tier-2 extraction and opt-in](https://github.com/kryptobaseddev/cleo/blob/84af0f9becd7b0f1279587cf3c85c793b76a5686/packages/core/src/sentient/propose-tick.ts#L1-L100), [readiness gated auto-promotion](https://github.com/kryptobaseddev/cleo/blob/84af0f9becd7b0f1279587cf3c85c793b76a5686/packages/core/src/sentient/propose-tick.ts#L640-L815), [owner acceptance commands](https://github.com/kryptobaseddev/cleo/blob/84af0f9becd7b0f1279587cf3c85c793b76a5686/packages/cleo/src/cli/commands/sentient.ts), [daemon Tier-2 schedule](https://github.com/kryptobaseddev/cleo/blob/84af0f9becd7b0f1279587cf3c85c793b76a5686/packages/core/src/sentient/daemon.ts#L875-L923).
- Basis: explicit and structural.
- Confidence: medium.
- Caveats: the included future capability is bounded to project work-queue adaptation, not a high-level environmental strategy. Tier-2 is **disabled by default**, generated titles are structured templates, some proposals remain grilled, Tier-3 autonomous merging is not credited. A model-backed BRAIN dream cycle stores knowledge, but alone does not prove independently selected strategic adaptation.

## S5 — Policy and identity

- State: —
- Function: no shipped system-identity/ultimate-policy dispute and closed legitimate S5 resolution path established at the CLEO project runtime recursion.
- Disturbance / variety regulated: conflicts over the project's ultimate charter as distinct from tool safety, task owner decisions or rollout policies.
- Decisive decision or feedback right: no such identity-level decision right demonstrated beyond operator intervention in current control/future candidate admission.
- Decision owner: none established for S5; repository maintainers, project owner, external agent vendors and OS users are distinct adjacent actors.
- Supporting / enforcement mechanisms: CANT agent roles/capability/ACL definitions, LOOM policy gates, owner attestation, kill-switch, Tier-2 enablement and contributor/release governance.
- Closure path: task admission, owner approval or kill-switch changes execution envelope but no separate ultimate-policy matter and returned identity decision is established.
- Why this is / is not agent-owned: an owner-named command or role topology does not automatically elevate normal permissions and risk choices into S5.
- Evidence: [CANT/LOOM boundary in README](https://github.com/kryptobaseddev/cleo/blob/84af0f9becd7b0f1279587cf3c85c793b76a5686/README.md), [owner attestation and restart](https://github.com/kryptobaseddev/cleo/blob/84af0f9becd7b0f1279587cf3c85c793b76a5686/packages/core/src/sentient/daemon.ts#L1135-L1164), [task ownership policies](https://github.com/kryptobaseddev/cleo/blob/84af0f9becd7b0f1279587cf3c85c793b76a5686/packages/core/src/task-work/claims.ts).
- Basis: structural.
- Confidence: medium.
- Caveats: the project owner's real-world legitimate authority is not denied; this scope has not reconstructed a distinct operational identity-policy path.

### Absence scope

- Surfaces inspected: owner kill/resume/revert attestation, CANT role rights, task admission and LOOM, protocol/readiness gates, local workspace config and public repository governance.
- Plausible first-party paths checked: owner policy toggles, signed receipts, agent capabilities, task-grill escalation, autonomous release and maintainer governance.
- Why no material first-party path remains: reviewed functions bind task and runtime safety, current work and prospect acceptance; none demonstrates a nonroutine ultimate identity dispute reaching and returning from a recognized S5 authority at this project recursion.

## Distributed OSS parent arrangement

Open-source contributors govern code/release changes under the repository's contribution rules. These actors are not silently the governing metasystem of an installed project team. The local owner is separately credited where current sentient daemon control (S3) and proposed future-task acceptance (S4) are supported.

## Self-hosted and non-human modes

CLEO stores project/session data locally and can launch configured third-party model agents. The daemon and Tier-2 require explicit enablement; the Pi runner is separately default off. The owner can shut down the unattended path. No autonomous merge or performance claim is credited merely from a template or experimental Tier-3 design.

## Recursion

Each spawned worker has a real distinct session and task lease but is not thereby a full viable recursive hierarchy. Project-scoped daemon operations and shared machine tool admission are different scopes; a global tool FIFO does not imply global S3 governance over multiple owners/projects.

## Variety and escalation

Agent/task variety is attenuated through session provenance, trusted claims, per-agent worktrees and a cross-process evidence-tool admission budget. Ordinary completion passes a separate deterministic source/test gate; failed claims return to retry/stuck accounting and may cause a daemon self-pause. The owner can intervene with kill/resume. New environmental signals can enter a future proposal path when Tier-2 is enabled and pass readiness/owner control before operational work.

## Evidence gaps

- S2 is a production deterministic inter-worker interference constructor; no model-driven resource-negotiation policy is inferred.
- S3* has unusually strong direct source/test verification but its mandatory same-production acceptance character does not establish a distinct complementary auditor.
- S4 is limited to opt-in future *task candidates*, not general strategic agency; Tier-3 autonomous merges, default-OFF Pi and hypothetical roadmap features are excluded.
- The upstream source is large; narrow credited paths were inspected at the immutable ref. No live external provider/model/daemon execution was performed.
- Node/pnpm were not installed on the inspection host, so upstream native TypeScript test suites could not be run. Index-local deterministic validation and GitHub CI are reported separately.
