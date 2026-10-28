---
harness_id: pragmatic-orchestration
project_name: Pragmatic Orchestration
repository: https://github.com/CodeAlive-AI/pragmatic-orchestration
review_ref: cc829d908822978fe7fce4670967525ea3a9a267
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

# Pragmatic Orchestration

## Review boundary

- System in focus: one installed Pragmatic Orchestration skill-and-`porch` environment in which a skill-capable model caller manages directly launched coding/research workers and can request separate model-led code audits; the companion `remote-agents` host skill is inspected as an optional deployment surface.
- Purpose and identity: give a coding model a first-party task-contract, delegation, supervision, steering, independent-review and acceptance operating protocol across supported external CLI model workers.
- Relevant environment: changing code/tasks, repository/workspace state, several vendor coding-agent processes, concurrent writer interference, incomplete outputs, provider turn/permission failures, model reviewer findings, and optional remote hosts.
- Standard-distribution boundary: published Agent Skills instructions, executable `skills/pragmatic-orchestration/scripts/porch` command, first-party delegate/review/steer/session runtimes, shipped configuration and their supported invocation by a model caller. External Codex/Claude/OpenCode/Grok/Devin/Gemini engines supply inference/execution but their unrelated internal organization is not attributed to Porch.
- Credited operating / distribution surfaces: `skills/pragmatic-orchestration/SKILL.md`, `references/delegate.md`, `references/review.md`, `references/review-acceptance.md`, `scripts/porch`, `scripts/lib/delegate.sh`, `scripts/lib/review_code.sh`, `scripts/lib/workflow_plans.py`, `scripts/lib/code_review_validate.py`, `scripts/lib/steer/{supervisor,control,mailbox,registry,adapters}*.py`, and the optional documented remote-host/visual-QA invocation path.
- Adjacent first-party surfaces excluded from ownership: author `AGENTS.md`/`CLAUDE.md`, test fakes and regression harness, demo videos, release/workflow CI, model selection advice and subscription comparisons, third-party provider metasystems, optional external visual-QA driver, and the companion `remote-agents` reference-only managed-worker daemon topology (no first-party daemon implementation is shipped).
- First-party operating / deployment modes considered: one or several managed local delegate runs (foreground/detached/steerable or deliberately one-shot); independent `review ask` and `review code` basic/specialists/super/ultra; user-provided separate workspaces for parallel writers; optional `remote-agents` host operations and read-only UI. These are alternative supported paths, not a claim they all run simultaneously.
- Recursion level: one model-caller-controlled project/work portfolio, with independently operating external coding agents as S1 subunits. Multiple independent OSS contributors and provider/vendor organizations are not a single Porch policy recursion.
- Reviewed revision: `cc829d908822978fe7fce4670967525ea3a9a267`.
- Observation date: 2026-10-28.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

The repository distributes a portable skill with a real `porch` CLI, not a resident all-purpose LLM or a fleet autopilot. The host's skill-capable model chooses tasks and invokes `porch delegate -a <exact-agent>`, which resolves a configured external CLI backend. The first-party Python supervisor binds one worker to one registry/run id, starts its backend adapter in the caller-selected working directory, captures normalized events, maintains durable result/artifact state and a private mailbox for steering/cancellation, and can keep a detached session alive beyond the caller's shell. `events`, `status`, `list`, `wait` and `wait-any` expose separate lifecycle, progress evidence and completed output; they do not automatically prove correctness. One-shot mode intentionally lacks mid-run steerability. Durable Codex continuation is opt-in and exact-session leased; it does not replay a failed turn blindly.

The skill supplies the *calling model's* operating rules: choose exact task/workspace scope, check substantive progress, interpret partial evidence, send bounded corrective steer, avoid two writers on the same working tree, decide whether to stop/reassign, and independently verify before acceptance. Separate `porch review` paths launch read-only model reviewers with direct source/diff access, explicit task-independent policies and role-specialized passes. Basic and specialists return independent findings without a synthesizer; super/ultra add deduplication and a further model judge. Source quotation validation is enforcement against unsupported citations, not an autonomous organizational decision by itself. The companion `remote-agents` skill operates remote hosts and can launch the same Porch workers; its described external ACP daemon and UI driver are not supplied here.

Primary source: [root README](https://github.com/CodeAlive-AI/pragmatic-orchestration/blob/cc829d908822978fe7fce4670967525ea3a9a267/README.md), [installed skill](https://github.com/CodeAlive-AI/pragmatic-orchestration/blob/cc829d908822978fe7fce4670967525ea3a9a267/skills/pragmatic-orchestration/SKILL.md), [delegate policy](https://github.com/CodeAlive-AI/pragmatic-orchestration/blob/cc829d908822978fe7fce4670967525ea3a9a267/skills/pragmatic-orchestration/references/delegate.md), [CLI dispatch](https://github.com/CodeAlive-AI/pragmatic-orchestration/blob/cc829d908822978fe7fce4670967525ea3a9a267/skills/pragmatic-orchestration/scripts/porch), [supervisor](https://github.com/CodeAlive-AI/pragmatic-orchestration/blob/cc829d908822978fe7fce4670967525ea3a9a267/skills/pragmatic-orchestration/scripts/lib/steer/supervisor.py), [remote skill](https://github.com/CodeAlive-AI/pragmatic-orchestration/blob/cc829d908822978fe7fce4670967525ea3a9a267/skills/remote-agents/SKILL.md).

## Operational model

A host model working on a real project selects one or several task-specific vendor coding agents, each of which decides how to inspect/implement/research its task with its own tool loop and returns evidence. The model caller owns the portfolio's task contracts, workspace allocation, checkpoint interpretation, corrective steering, cancellation/replacement, and acceptance of actual changes. The CLI enforces exact-run control and honest delivery acknowledgments, but has no autonomous project-priority scheduler. When multiple writers might overlap, the skill explicitly requires separate user-authorized workspaces and refuses implicit workspace creation; after interruption, the caller must confirm old writer termination and inspect its partial state before replacing it. The separate reviewers are tasked to audit direct repository/diff evidence under independent, read-only prompts and return findings to the caller for acceptance/correction. Optional remote-host setup supplies transport and isolation, not a second hidden owner of project-level control.

## S1 — Operations

- State: A
- Function: independent model-directed coding, codebase research and validation inside a bounded delegated task, including normal host-model task work when no external worker is needed.
- Disturbance / variety regulated: changing source and requirements, implementation choices, test/tool feedback and partial failures within one assigned workspace and task contract.
- Decisive decision or feedback right: the selected external coding-agent model chooses investigation, edits, tools, tests and substantive answer inside its assigned scope; the caller model chooses the task contract and later acceptance but does not precompute every worker action.
- Decision owner: configured Codex/Claude/OpenCode/Grok/Devin model actor in each actual delegated CLI session; a supported skill-capable host model owns its own nondelegated task decisions.
- Supporting / enforcement mechanisms: `porch delegate` agent selection, backend adapters, configured model/profile, prompt transport, exact cwd, session/result artifacts, supervisor/registry, bounded status and final-result delivery; external provider models supply inference rather than Porch-owned hidden capabilities.
- Closure path: host model assigns a bounded objective → backend model executes its own task/tool feedback loop → code/research/check result and evidence return through the supervisor → calling model checks/accepts or steers/reassigns unfinished work.
- Boundary reachability: `SKILL.md` routes installed skill-capable callers to the shipped executable `porch` entrypoint, whose `delegate` dispatcher, Python supervisor and adapters genuinely start the configured worker; this is an advertised real use path, not a test-only fake agent.
- Why this is / is not agent-owned: without a model-driven worker, the wrapper can transport tasks and persist events but cannot select the task-specific actions or produce substantive code; without the caller model, the skill does not itself choose the task contract.
- Evidence: [installed skill delegation map](https://github.com/CodeAlive-AI/pragmatic-orchestration/blob/cc829d908822978fe7fce4670967525ea3a9a267/skills/pragmatic-orchestration/SKILL.md), [delegate launcher](https://github.com/CodeAlive-AI/pragmatic-orchestration/blob/cc829d908822978fe7fce4670967525ea3a9a267/skills/pragmatic-orchestration/scripts/lib/delegate.sh), [supervisor and adapter invocation](https://github.com/CodeAlive-AI/pragmatic-orchestration/blob/cc829d908822978fe7fce4670967525ea3a9a267/skills/pragmatic-orchestration/scripts/lib/steer/supervisor.py), [delegate runtime](https://github.com/CodeAlive-AI/pragmatic-orchestration/blob/cc829d908822978fe7fce4670967525ea3a9a267/skills/pragmatic-orchestration/references/delegate-runtime.md).
- Basis: explicit and structural.
- Confidence: high for shipped model/task/runtime connection; no live provider invocation was attempted.
- Caveats: the actual provider binary, account/quota and selected skill-capable host are external installation dependencies. Do not infer provider-internal multi-agent coordination as Porch S2/S3.

## S2 — Coordination

- State: A
- Function: attenuation of conflicts between independently writing S1 agents during overlapping project delegation and corrective replacement.
- Disturbance / variety regulated: concurrent writes to the same mutable checkout, a successor modifying partially written files before its predecessor is actually stopped, and different task scopes modifying each other's work.
- Decisive decision or feedback right: the model caller gives disjoint task scopes and uses distinct user-authorized workspaces for concurrent writers; when new events/diffs expose conflict or failure, it decides whether to redirect/stop an exact worker, preserve partial changes, or withhold a replacement assignment until the writer is confirmed stopped.
- Decision owner: the skill-guided calling model in the supported multi-delegate mode. The user has prior authority over workspace creation; the supervisor/registry only enforces run-addressed lifecycle and transport.
- Supporting / enforcement mechanisms: separate user-provided working directories, explicit task scope contracts, run IDs, `delegate list`/`events`/`status`/`cancel`/`steer`, stop/acknowledgment verification, VCS status and diff checks, and the first-party overlapping-writer guard in delegation policy.
- Closure path: two model worker tasks could contend for one checkout → model caller assigns distinct approved workspaces or keeps the replacement waiting → observes run outcomes/partial diffs → sends corrective steer or cancels and confirms terminal status → only then permits the next conflicting S1 writer to act.
- Boundary reachability: the shipped skill has explicit multi-worker/parallel-writer and stop-before-reassignment instructions while `porch` exposes independent running worker IDs, separate cwd binding, observation and targeted intervention. This is a supported optional multiple-delegate operating arrangement, conditional on user-authorized workspaces.
- Why this is / is not agent-owned: the caller model judges actual overlap and which worker/scope to change; the private registry prevents mis-addressed control messages but does not detect or autonomously resolve file conflicts.
- Distinct S1 units: at least two independently executing coding agents each with a separate model/tool loop and one assigned project task/working directory.
- Inter-S1 disturbance: simultaneous unrelated writers on one checkout can overwrite, intermix or invalidate changes; premature reassignment into a predecessor's partially modified tree repeats the conflict.
- Attenuating coordination relation: first-party mandatory separate-workspace/clear-scope policy plus substantive parent checkpointing, explicit stop/verify before conflicting replacement, and corrective steering into subsequent tasks.
- Feedback into subsequent S1 behaviour: run event/cancellation outcome and inspected repository diff go to the model caller; it changes the next worker's root/scope, or sends the exact active worker a corrective task before continuing.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the skill identifies a concrete inter-writer contention hazard and prescribes an operational anti-overlap/feedback relation among distinct worker loops, not merely a mailbox or job queue.
- Evidence: [delegate multi-writer and replacement contract](https://github.com/CodeAlive-AI/pragmatic-orchestration/blob/cc829d908822978fe7fce4670967525ea3a9a267/skills/pragmatic-orchestration/references/delegate.md), [parent skill contract](https://github.com/CodeAlive-AI/pragmatic-orchestration/blob/cc829d908822978fe7fce4670967525ea3a9a267/skills/pragmatic-orchestration/SKILL.md), [run-addressed control commands](https://github.com/CodeAlive-AI/pragmatic-orchestration/blob/cc829d908822978fe7fce4670967525ea3a9a267/skills/pragmatic-orchestration/scripts/lib/steer/control.py), [remote workspace guidance](https://github.com/CodeAlive-AI/pragmatic-orchestration/blob/cc829d908822978fe7fce4670967525ea3a9a267/skills/remote-agents/references/porch-remote.md).
- Basis: explicit operating contract backed by active run-addressed tools.
- Confidence: medium: model-owned preventive and corrective protocol is shipped, but there is no automatic cross-workspace write-collision detector or proof that callers always follow the skill.
- Caveats: single-delegate or manually co-located writers do not realize this S2 path. Runtime locks protect metadata/mailboxes, not shared repository writes; user must authorize separate writer workspaces.

## S3 — Inside-and-now control

- State: A
- Function: model-caller regulation of the whole current delegated project workload and commitments through project supervision, intervention and acceptance.
- Disturbance / variety regulated: stalled worker progress, wrong task interpretations, partial or failed outcomes, unexpected deviations, competing active work, uncertainty over delivery/steering and incomplete acceptance criteria.
- Decisive decision or feedback right: the calling model evaluates the active delegation portfolio and substantive evidence, chooses new assignments/reprioritization, corrective steering, cancellation, reassignment and whether work is accepted or requires further verification.
- Decision owner: the operating skill-capable host model in its agent-orchestrator mode; CLI lifecycle commands are instruments and user scope constraints remain binding.
- Supporting / enforcement mechanisms: current run enumeration, `events` cursors, `wait-any` group snapshots, per-run complete final texts, exact steer delivery status, deviation journals, verified tests/diffs and optional remote-host status.
- Closure path: several active worker status/progress/evidence streams → host model forms current project-wide judgment → targeted steer, cancel, replacement, revised workload or acceptance → subsequent worker execution/commitments and verification change.
- Boundary reachability: the installed skill expressly directs the model caller to inspect each worker during its first minute, adapt later supervision, keep the parent turn active, observe several runs and make intervention/acceptance decisions; all named control/observation commands are routed to shipped CLI and supervisor.
- Why this is / is not agent-owned: model discretion determines current priorities, whether the work is useful, scope of corrective action and acceptance. A process exit, heartbeat, quota readout or `wait-any` timeout alone would not make that judgment.
- Whole-system current view: `delegate list --active` enumerates the private run registry, while `wait-any` reports complete supplied-group state/timing and `events`/artifacts provide substantive per-worker evidence; the calling model must retain the project group membership rather than infer it from a global list.
- Current-control decision scope: allocate distinct worker contracts, redirect exact active sessions, stop unproductive work, delay conflicting replacement, coordinate completion and accept/reject worker contributions against task criteria.
- Evidence: [model caller supervision and acceptance contract](https://github.com/CodeAlive-AI/pragmatic-orchestration/blob/cc829d908822978fe7fce4670967525ea3a9a267/skills/pragmatic-orchestration/references/delegate.md), [group wait and event interfaces](https://github.com/CodeAlive-AI/pragmatic-orchestration/blob/cc829d908822978fe7fce4670967525ea3a9a267/skills/pragmatic-orchestration/references/delegate-runtime.md), [registry control](https://github.com/CodeAlive-AI/pragmatic-orchestration/blob/cc829d908822978fe7fce4670967525ea3a9a267/skills/pragmatic-orchestration/scripts/lib/steer/control.py), [parent-owned review acceptance](https://github.com/CodeAlive-AI/pragmatic-orchestration/blob/cc829d908822978fe7fce4670967525ea3a9a267/skills/pragmatic-orchestration/references/review-acceptance.md).
- Basis: explicit and structural.
- Confidence: medium-high for model-run supported project supervision, absent end-to-end provider session observation.
- Caveats: neither the CLI nor optional read-only UI has autonomous whole-fleet scheduling, and a human issuing an occasional CLI stop is not enough to establish a separate operational parent-governed S3 mode. Periodic checks are a caller obligation, not a built-in timer.

## S3* — Complementary audit

- State: A
- Function: independent, direct-evidence auditing of implementation/correctness/security claims from worker work, with corrective results fed to the caller.
- Disturbance / variety regulated: false completion reports, unsafe patches, stale or invented code quotations, defects not visible in a worker's self-summary, and one actor rubber-stamping its own work.
- Decisive decision or feedback right: a separately launched read-only reviewer model assesses the actual source/diff and reports independently reasoned defects; optionally an independent judge model adjudicates combined discoveries, while the calling model chooses corrective disposition.
- Decision owner: one or several review-mode model agents operating under the first-party audit prompt rather than the implementing worker's instruction/authority, followed by the caller model for remedial action.
- Supporting / enforcement mechanisms: `review code` direct file/diff input, role-specific security/correctness and optional specialist passes, read-only review contract, per-pass independent reports, cross-check of quoted code against files, optional deterministic dedup and separate LLM judge, final report delivery.
- Closure path: worker claims a change is correct/ready → independent review model directly inspects the file/diff and broadens relevant source context → source-anchored findings reach the caller → caller verifies and commands corrective work, targeted tests, or reasoned acceptance before completion.
- Boundary reachability: `porch review code` basic is an ordinary shipped CLI mode, and `review ask`/super/ultra are explicit supported modes. The skill instructs the host caller to invoke reviewers separately, supply task contracts, and act on findings; no private maintainer CI reviewer is borrowed.
- Why this is / is not agent-owned: distinct reviewing model agents make risk/finding judgments from independent direct access; quote checking/dedup scripts only validate or combine evidence, while the primary worker cannot rewrite those review judgments through its own completion message.
- Claim being audited: a delegated coding agent's implementation/report or the caller's proposed code change satisfies task and security/correctness requirements.
- Ordinary reporting path: implementing worker's session events, final answer, own tests and source changes return to its calling model through `delegate wait`.
- Complementary access path: independent `review code` reader receives current source file/diff plus an explicitly incomplete seed and is required to expand its own repository search; findings carry file/line/quoted-code anchors checked against source.
- Independence boundary: reviewers are separately invoked read-only model sessions with dedicated audit roles and denied edits/delegation; they are not the working delegate's self-attestation. Sharing vendor/model family or an agent-selected initial file seed does not itself guarantee diversity; optional judge is another audit pass, not substitute evidence.
- Who acts on findings: the calling orchestration model verifies dispositions against the task contract and steers/assigns corrections; neither basic/specialist report nor automatic judge verdict unilaterally accepts worker changes.
- Evidence: [review operational mode](https://github.com/CodeAlive-AI/pragmatic-orchestration/blob/cc829d908822978fe7fce4670967525ea3a9a267/skills/pragmatic-orchestration/references/review.md), [specialist review dispatch](https://github.com/CodeAlive-AI/pragmatic-orchestration/blob/cc829d908822978fe7fce4670967525ea3a9a267/skills/pragmatic-orchestration/scripts/lib/review_code.sh), [quote validation](https://github.com/CodeAlive-AI/pragmatic-orchestration/blob/cc829d908822978fe7fce4670967525ea3a9a267/skills/pragmatic-orchestration/scripts/lib/code_review_validate.py), [review workflow stages](https://github.com/CodeAlive-AI/pragmatic-orchestration/blob/cc829d908822978fe7fce4670967525ea3a9a267/skills/pragmatic-orchestration/scripts/lib/workflow_plans.py), [task-relative remediation](https://github.com/CodeAlive-AI/pragmatic-orchestration/blob/cc829d908822978fe7fce4670967525ea3a9a267/skills/pragmatic-orchestration/references/review-acceptance.md).
- Basis: explicit and structural.
- Confidence: medium-high for operational independence and direct-source audit; no live reviewers were paid/run at the frozen source.
- Caveats: optional review must actually be invoked for a particular task; basic/specialists do not have an internal judge, and no automated merge gate forces a review finding to block acceptance. Read-only enforcement varies by backend.

## S4 — Outside-and-then intelligence

- State: —
- Function: no supported first-party organizational loop that senses changing external/future conditions, develops strategic alternatives and returns a capability adaptation decision into the whole current system.
- Disturbance / variety regulated: potential changes in future provider quality, coding technology, cost, environment or long-horizon deployment capability are discussed, but not closed through a shipped prospective sensing/adaptation process.
- Decisive decision or feedback right: not supplied for S4; a caller can manually choose another model/provider or alter configuration, and retrospective session history can inform ad hoc choices, without a distinct future-oriented intelligence owner and returned capability-change loop.
- Decision owner: no autonomous or legitimate parent S4 decision owner is established within this distribution boundary.
- Supporting / enforcement mechanisms: provider/profile configuration, quota snapshots, session history `stats`/`flags`, advice to periodically inspect agent effectiveness, external-model comparison tips and remote-host provisioning helpers.
- Closure path: no demonstrated outside-and-then sensing → alternative-generation → adaptation decision → changed future capability/S3 closure; ordinary task replanning and same-run steering are S3, not S4.
- Why this is / is not agent-owned: an optional model's analysis of past sessions could be extended into strategy, but the installed skill does not bind that analysis to first-party prospective adaptation authority and returned operating-capability change.
- Evidence: [skill review/delegation modes](https://github.com/CodeAlive-AI/pragmatic-orchestration/blob/cc829d908822978fe7fce4670967525ea3a9a267/skills/pragmatic-orchestration/SKILL.md), [session-history tools](https://github.com/CodeAlive-AI/pragmatic-orchestration/blob/cc829d908822978fe7fce4670967525ea3a9a267/skills/pragmatic-orchestration/references/session-history.md), [configuration and quota](https://github.com/CodeAlive-AI/pragmatic-orchestration/blob/cc829d908822978fe7fce4670967525ea3a9a267/skills/pragmatic-orchestration/references/configuration.md), [remote-host options](https://github.com/CodeAlive-AI/pragmatic-orchestration/blob/cc829d908822978fe7fce4670967525ea3a9a267/skills/remote-agents/SKILL.md).
- Basis: bounded first-party absence.
- Confidence: medium-high within current shipped operational paths.
- Caveats: a user-built future-planning program or another organization's S4 could consume Porch telemetry, but is not a supplied first-party S4 constructor merely because telemetry exists.

### Absence scope

- Surfaces inspected: skill instructions and task policy, `sessions.py`/history reference, quota and profile config, review/steer flows, optional remote-host/onboarding guidance and model comparison advice.
- Plausible first-party paths checked: session effectiveness reflection and stats, quota-aware provider choice, periodic model quality advice, remote fleet changes and longer-term Codex session continuation.
- Why no material first-party path remains: these expose retrospective evidence, budget constraints, ordinary task continuation or manual setup, not a shipped model/parent loop for prospective environmental intelligence, adaptation-option judgment and return into ongoing system capability.

## S5 — Policy and identity

- State: —
- Function: no first-party identity-level or ultimate-policy adjudication mechanism with legitimate decisive ownership and returned governance of Porch operation.
- Disturbance / variety regulated: competing permissible operating boundaries, provider identities, security exposure and project goals are limited by human-owned installation/configuration/task contracts, not resolved by a Porch ultimate-policy institution.
- Decisive decision or feedback right: caller/user chooses task scope, external agent accounts, writable roots and provider configuration; per-run permission errors and acceptance decisions do not become identity-level policy arbitration.
- Decision owner: no supported autonomous S5 owner or closed parent-governed S5 mode for the whole assessed system is evidenced.
- Supporting / enforcement mechanisms: review read-only prompt, role/tool restrictions where provider supports them, external credentials/config, remote host security hardening, user authorization before parallel writer workspaces and ordinary acceptance criteria.
- Closure path: provider permission refusal or task-scope concern → caller/user decision over that *task*; no shipped identity/ultimate-policy issue → legitimate top-level arbitration → authoritative update → subsequent Porch charter enforcement loop.
- Why this is / is not agent-owned: Porch has operational guardrails and user-set credentials/roots; a model applying those constraints does not author its own ultimate identity, and the parent can configure the tool without performing a defined S5 return loop.
- Evidence: [skill operating limits](https://github.com/CodeAlive-AI/pragmatic-orchestration/blob/cc829d908822978fe7fce4670967525ea3a9a267/skills/pragmatic-orchestration/SKILL.md), [delegate authorization/workspace contract](https://github.com/CodeAlive-AI/pragmatic-orchestration/blob/cc829d908822978fe7fce4670967525ea3a9a267/skills/pragmatic-orchestration/references/delegate.md), [configuration](https://github.com/CodeAlive-AI/pragmatic-orchestration/blob/cc829d908822978fe7fce4670967525ea3a9a267/skills/pragmatic-orchestration/references/configuration.md), [remote host security](https://github.com/CodeAlive-AI/pragmatic-orchestration/blob/cc829d908822978fe7fce4670967525ea3a9a267/skills/remote-agents/references/security.md).
- Basis: bounded first-party absence.
- Confidence: high for absence of a defined identity authority path among inspected shipped runtime and policy surfaces.
- Caveats: maintainers and users can revise the published skill, but contribution governance and configuration change are not a first-party operational S5 closure at this system recursion.

### Absence scope

- Surfaces inspected: installed `SKILL.md`/operating contract, `config.example.json`, backend permission and role contracts, delegate/review policy, remote-agent host security instructions and adjacent maintainer materials.
- Plausible first-party paths checked: user permission prompts, readonly reviewer rules, host security policy, operator configuration, runtime takeover/cancellation and distributed open-source project governance.
- Why no material first-party path remains: none supplies a distinct legitimate decisive ultimate-policy forum and returned charter/identity judgment for the operating project; these are task authorization, provider-side enforcement, host setup or external maintainer authority.

## Recursion

The declared system is the model caller's actual project portfolio, not the aggregated global population of all Porch installations or all external vendor agents. Each delegated worker is S1 at this level. The skill's one-run supervisor is below the portfolio-control level; its private mailbox and registry do not independently own S3. The model reviewer runs are complementary audit participants, not necessarily more S1 writers. A remote host can contain workers but the distributed external host administrator and the reference-only ACP daemon are not silently counted as additional Porch S4/S5 owners.

## Variety and escalation

Portability across model CLI backends, detached runs and asynchronous steering increase the caller's operational variety; the host model must correctly interpret honest distinction between accepted, delivered and substantively applied guidance. A failed worker, denied provider permission or missing completion evidence returns to the model caller for a bounded new task/correction; material user-scope changes return to the actual user. Reviewers can independently find defects, but a reviewer report by itself does not change code or grant publication permission. Future strategy or identity disputes lack a first-party defined authority loop and remain outside this classified recursion.

## Evidence gaps

- The static code and local fake transport tests cannot establish end-to-end quality of arbitrary external model decisions, secure read-only enforcement in every vendor CLI, or effective compliance by a host model with the skill's multi-writer policy.
- S2's `A` depends on a genuinely skill-guided model caller supervising at least two separate S1 writers with user-approved workspaces; no automatic repository collision sensor is claimed.
- S3*'s independent direct-source reviewer path is shipped but task-opt-in. No actual provider-backed reviewer ran for this frozen revision.
- The `remote-agents` reference-only daemon topology and external Windows visual driver are excluded from credited live first-party ownership. They may require separate future review if shipped as executable orchestration services.
