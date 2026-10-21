---
harness_id: politik
project_name: Politik
repository: https://github.com/cordfuse/politik
review_ref: c1fa7312c75599d72b187bf20088f51f5dda2247
reviewed_at: 2026-10-21
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
assessment_changed_at: 2026-10-21
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: P
---

# Politik

**Canonical included** source-first general VSM assessment for [Index batch #1827](https://github.com/opensiro/vsm-harness-index/issues/1827) row 3, frozen from intake #1281 position 6. Admitted canonical vector `A / — / — / — / — / P`. Assessment is grounded in this first-party CLI's concrete run mode and constitutionally bounded human authority, not the README's ambition of a permanent, self-governing enterprise of agents.

## Review boundary

- System in focus: one local Politik git-backed governed session using the shipped Node/TypeScript CLI and optional hosted SCM projection, with stateless third-party-model worker turns.
- Purpose and identity: convene and record role-limited AI/human decision and work sessions under an explicit Charter, a human constitutional Speaker, structured voting and audit records.
- Relevant environment: human session Speaker, participants/agent CLIs, git checkout, optional GitHub SCM, OS subprocess, configuration and command-line tools.
- Standard-distribution boundary: published `@cordfuse/politik` Node command and `src/{runner,agents,spawn,charter,division,escalation,cli,...}.ts` in a configured session. Real external LLM CLI is a named execution dependency, not a separate first-party business team. No server/fleet coordination beyond this shipped run boundary.
- Credited operating / distribution surfaces: `bin/politik.js`, `src/cli.ts`, `src/runner.ts`, `src/agents.ts`, `src/spawn.ts`, `src/election.ts`, `src/charter.ts`, `src/division.ts`, `src/escalation.ts`, `src/state.ts` and git-backed record/lock/ledger utilities.
- Adjacent first-party surfaces excluded from ownership: protocol reference examples, research/game theory projections, repo developer CI/tests, conceptual architecture claims of across-machine/cross-organization fleet control and optional GitHub hosting that lacks a distinct first-party model worker.
- First-party operating / deployment modes considered: standalone git session, CLI-run one-off agent turn, multi-turn governance process, optional SCM-projected approval/merge, single session and documented local nested sessions.
- Recursion level: one governed git session and its stateless role turns, not a continuing autonomous multi-departmental organization.
- Reviewed revision: c1fa7312c75599d72b187bf20088f51f5dda2247.
- Observation date: 2026-10-21.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

`cli.ts` exposes session init/scaffold, `politik run`, Division vote/tally, Assent, Point of Order and nested-session reports. The concrete `runner.ts::runTurn` checks a `CONVENED` session and parseable `CHARTER.md`, verifies constituency slots, performs election/lock, composes the current task with Standing Orders and recent Hansard, and invokes `spawnAgent` with a known executable adapter from `agents.ts`. Model output and side effects become git changes, Hansard, result/elapsed usage records and optional session suspension. The code acknowledges containment is **detected after** a potentially privileged process has run, not guaranteed OS isolation. Source: https://github.com/cordfuse/politik/blob/c1fa7312c75599d72b187bf20088f51f5dda2247/src/runner.ts; https://github.com/cordfuse/politik/blob/c1fa7312c75599d72b187bf20088f51f5dda2247/src/agents.ts; https://github.com/cordfuse/politik/blob/c1fa7312c75599d72b187bf20088f51f5dda2247/src/spawn.ts; https://github.com/cordfuse/politik/blob/c1fa7312c75599d72b187bf20088f51f5dda2247/src/charter.ts; https://github.com/cordfuse/politik/blob/c1fa7312c75599d72b187bf20088f51f5dda2247/src/containment.ts.

A Division proposes/casts/tallies votes under a protocol, but its carried result is not enacted until `ASSENT`, which is bound to a specified role and recorded in git; an optional SCM provider can project an enacted motion into a pull-request merge. A Point of Order can suspend a session and requires an authorized Speaker ruling to resume; the next `runTurn` reads new state, Charter, and recent record. Hansard is an immutable-intended git narrative and LEDGER records cost; neither is independently cognitive. Source: https://github.com/cordfuse/politik/blob/c1fa7312c75599d72b187bf20088f51f5dda2247/src/division.ts; https://github.com/cordfuse/politik/blob/c1fa7312c75599d72b187bf20088f51f5dda2247/src/cli.ts; https://github.com/cordfuse/politik/blob/c1fa7312c75599d72b187bf20088f51f5dda2247/src/escalation.ts; https://github.com/cordfuse/politik/blob/c1fa7312c75599d72b187bf20088f51f5dda2247/src/runner.ts; https://github.com/cordfuse/politik/blob/c1fa7312c75599d72b187bf20088f51f5dda2247/src/integrity.ts.

## Operational model

Operator writes/accepts session Charter → convenes session and task → first-party `runTurn` checks session/role and produces bounded prompt → external CLI-hosted model agent chooses task-specific content/actions and makes git changes → runner records result and ledger, may suspend on escalation → authorized human decisions/votes/rulings return through session state, Charter and Hansard to later worker turns. This is an actual shipped agent-operation constructor with a concrete tool-feedback record, but still only one short-lived worker session at a time, not proven multiple continuing independent S1 cells. Model/provider computation is external; coordination/record/permission functionality is first-party.

## S1 — Operations

- State: A
- Function: Perform semantic task work inside a governed session using a model-enabled, stateless role worker.
- Disturbance / variety regulated: Unstructured draft/governance/task requirements, tool results and git work needing substantive model interpretation.
- Decisive decision or feedback right: Worker chooses content and permissible git/tool actions for the task; human retains higher-level assent/constitutional rights.
- Decision owner: The model-backed worker launched by the first-party Politik runner and scoped to a session, role, standing orders and constituency.
- Supporting / enforcement mechanisms: Known CLI registry, election/lock, session state/Charter gate, prompt composer, subprocess adapter, Hansard/LEDGER records.
- Closure path: `runTurn` → `spawnAgent` → result/files committed or inspected → Hansard/state and subsequent prompts consume retained results/record; point-of-order can suspend further work.
- Boundary reachability: `src/cli.ts` command `politik run` invokes `runTurn` which invokes the real subprocess adapter using supported Claude Code/Codex/etc command definitions. It does not require an unpublished first-party autonomous service.
- Why this is / is not agent-owned: The task-semantic model worker is executed in a first-party session path, not merely described in a prompt example; process remains external inference but operated within shipped session orchestration.
- Evidence: https://github.com/cordfuse/politik/blob/c1fa7312c75599d72b187bf20088f51f5dda2247/src/cli.ts; https://github.com/cordfuse/politik/blob/c1fa7312c75599d72b187bf20088f51f5dda2247/src/runner.ts; https://github.com/cordfuse/politik/blob/c1fa7312c75599d72b187bf20088f51f5dda2247/src/agents.ts; https://github.com/cordfuse/politik/blob/c1fa7312c75599d72b187bf20088f51f5dda2247/src/spawn.ts; https://github.com/cordfuse/politik/blob/c1fa7312c75599d72b187bf20088f51f5dda2247/README.md
- Basis: explicit and structural.
- Confidence: high.
- Caveats: Source-level runnable path, not a live AI experiment or proof of physical-world effect; full OS sandbox containment is not claimed..




## S2 — Coordination

- State: —
- Function: No evidenced continuing inter-S1 operational-unit interference regulated by reciprocal feedback.
- Disturbance / variety regulated: Contention for constituency seats and disagreement in a Division, not automatically conflict between continuing viable operational departments.
- Decisive decision or feedback right: A candidate S2 should resolve a concrete inter-S1 disturbance and return adjustment to future independent operations.
- Decision owner: Election/slot lock, protocol vote tally and Speaker handle governance work, not proven S2 discretionary owner across continuing agentic S1 units.
- Supporting / enforcement mechanisms: `nodeLockFs`, constituency election, quorum/Division, Hansard, nested session registry.
- Closure path: Slot election admits or defers one stateless worker turn; vote tally and Assent decide a motion. Neither closes an interference-feedback relation between multiple continuing S1 operations.
- Boundary reachability: No positive state.
- Why this is / is not agent-owned: Session concurrency/seat contention and voting are real mechanisms but do not constitute a demonstrated S2-specific regulation across two viable agentic operating units at this declared boundary.
- Evidence: https://github.com/cordfuse/politik/blob/c1fa7312c75599d72b187bf20088f51f5dda2247/src/runner.ts; https://github.com/cordfuse/politik/blob/c1fa7312c75599d72b187bf20088f51f5dda2247/src/election.ts; https://github.com/cordfuse/politik/blob/c1fa7312c75599d72b187bf20088f51f5dda2247/src/division.ts; https://github.com/cordfuse/politik/blob/c1fa7312c75599d72b187bf20088f51f5dda2247/src/federation.ts
- Basis: structural.
- Confidence: moderate-high.
- Caveats: A future service with continuously operating teams and concrete reciprocal collision handling would require a new pinned assessment..


### Absence scope

- Surfaces inspected: Current published runner, election/seat lock, vote/tally, nested registry and task record.
- Plausible first-party paths checked: Constituency conflicts, concurrent subagent activities, quorum disagreements and nested cross-session work.
- Why no material first-party path remains: A session runs discrete worker turns and governance votes; no pair of continuing, viable first-party S1 cells with an actual or structurally specific operational interference and closed attenuating response was found.


## S3 — Inside-and-now control

- State: —
- Function: No ongoing whole-system management of present operational resources, commitments or interventions across independent continuing S1 units is established.
- Disturbance / variety regulated: Agent cost/time bounds, task execution and governance vote disagreements.
- Decisive decision or feedback right: Whole-of-organization current control would decide resource/accountability interventions and return them into S1 operation.
- Decision owner: Runtime enforces Charter limits; Speaker enacts motions but these are not shown as continuous whole-fleet S3 budget/priority bargaining across operating departments.
- Supporting / enforcement mechanisms: Endurance limits, cost LEDGER, deterministic sessions, quorum, suspension and actor constraints.
- Closure path: Runtime may deny/stop one session, and a human may assent, but the reviewed reference has no instantiated whole-organization present performance-control loop.
- Boundary reachability: No positive S3 or parent S3 mode.
- Why this is / is not agent-owned: Static per-session cost ceilings and authorized motions cannot be promoted to ongoing S3 of a multi-S1 organization without present whole-system decision evidence.
- Evidence: https://github.com/cordfuse/politik/blob/c1fa7312c75599d72b187bf20088f51f5dda2247/src/runner.ts; https://github.com/cordfuse/politik/blob/c1fa7312c75599d72b187bf20088f51f5dda2247/src/charter.ts; https://github.com/cordfuse/politik/blob/c1fa7312c75599d72b187bf20088f51f5dda2247/src/ledger.ts; https://github.com/cordfuse/politik/blob/c1fa7312c75599d72b187bf20088f51f5dda2247/src/cli.ts; https://github.com/cordfuse/politik/blob/c1fa7312c75599d72b187bf20088f51f5dda2247/POLITIK-ARCHITECTURE.md
- Basis: structural.
- Confidence: moderate-high.
- Caveats: Real governance/approval mechanisms exist; this negative is specific to their lack of the required whole-current S3 regulation at the declared recursion..


### Absence scope

- Surfaces inspected: Execution, session lifecycle, Charter cost/quorum controls, agents, nested tree and provider projections.
- Plausible first-party paths checked: Cross-operational resource allocation, priority changes and managerial intervention affecting multiple continuing agent work cells.
- Why no material first-party path remains: All inspected decision paths regulate a session/protocol motion or finite turn; neither a continuing whole-system managerial owner nor a returned inter-unit resource/commitment regulation loop was demonstrated.


## S3* — Complementary audit

- State: —
- Function: No independent complementary audit of an S3 whole-system managerial account is operationally returned to current control.
- Disturbance / variety regulated: Coerced exits, strategic withdrawals, manipulated governance records or false agent reports.
- Decisive decision or feedback right: Inspect reality by an alternative channel, reach independent judgment and feed findings to S3 correction.
- Decision owner: Pure `reviewIntegrity` detects patterns in the same Hansard and surfaces reports; Speaker judgment about what to do is separate and not shown as a complementary audit-into-S3 loop.
- Supporting / enforcement mechanisms: Append-only-intended Hansard/git commit history, integrity checks, immutable ledger, containment-after-execution detection.
- Closure path: Integrity findings can be printed/surfaced, but source does not establish a distinct independent alternative access path, manager accountability and corrective S3 operation from them.
- Boundary reachability: No positive state.
- Why this is / is not agent-owned: Verification against the ordinary governance record, even valuable bad-faith pattern detection, is not independent complementary S3 audit at the session recursion.
- Evidence: https://github.com/cordfuse/politik/blob/c1fa7312c75599d72b187bf20088f51f5dda2247/src/integrity.ts; https://github.com/cordfuse/politik/blob/c1fa7312c75599d72b187bf20088f51f5dda2247/src/runner.ts; https://github.com/cordfuse/politik/blob/c1fa7312c75599d72b187bf20088f51f5dda2247/src/ledger.ts; https://github.com/cordfuse/politik/blob/c1fa7312c75599d72b187bf20088f51f5dda2247/src/escalation.ts
- Basis: structural.
- Confidence: moderate-high.
- Caveats: The record includes meaningful attribution and fraud signals; these are not negated by withholding S3*..


### Absence scope

- Surfaces inspected: Integrity function, Hansard, LEDGER, containment check, Speaker escalation flow.
- Plausible first-party paths checked: Alternative operational inspection/ground truth beyond the same Hansard; audit owner and corrective whole-current manager response.
- Why no material first-party path remains: The shipped detector consumes regular governance records and reports patterns; no S3-facing independent audit judgment/return loop is evidenced.


## S4 — Outside-and-then intelligence

- State: —
- Function: No shipped prospective external-environment intelligence loop selecting organizational adaptation options and returning them into present capability.
- Disturbance / variety regulated: Potential changes in protocol context and future risks beyond the current motion/task.
- Decisive decision or feedback right: Identify environmental change and prospective options, then engage present S3 for accepted capability change.
- Decision owner: Per-session agent may research a commissioned task, while protocol choice and Charter terms are configured by humans.
- Supporting / enforcement mechanisms: Reference protocols, optional SCM projection, session registry, research/game-theoretic conceptual notes.
- Closure path: Agents can formulate motions/current plans, but no first-party external future monitoring/option-generation/adoption feedback loop is wired into present system capability.
- Boundary reachability: No positive state.
- Why this is / is not agent-owned: Current political deliberation and research design are not by themselves S4 of the harness; game theory experiments explicitly remain future research.
- Evidence: https://github.com/cordfuse/politik/blob/c1fa7312c75599d72b187bf20088f51f5dda2247/README.md; https://github.com/cordfuse/politik/blob/c1fa7312c75599d72b187bf20088f51f5dda2247/RESEARCH.md; https://github.com/cordfuse/politik/blob/c1fa7312c75599d72b187bf20088f51f5dda2247/src/runner.ts; https://github.com/cordfuse/politik/blob/c1fa7312c75599d72b187bf20088f51f5dda2247/src/protocol.ts; https://github.com/cordfuse/politik/blob/c1fa7312c75599d72b187bf20088f51f5dda2247/src/cli.ts
- Basis: explicit and structural.
- Confidence: high.
- Caveats: An agent may write prospective content as an S1 task outcome; that is not an organizational adaptation capability..


### Absence scope

- Surfaces inspected: Runner, source-level protocol registration, nested-session registry, research agenda and optional SCM adapters.
- Plausible first-party paths checked: Externally oriented monitoring, prospective alternatives, adoption by S3 and changes to next agent capabilities.
- Why no material first-party path remains: No material shipped path cycles environmental intelligence through option development into changed current operating capability; research/game theory is declared not built.


## S5 — Policy and identity

- State: P
- Function: Human constitutional Speaker establishes binding session identity/standing orders and closes escalated identity/policy questions at the declared session recursion.
- Disturbance / variety regulated: Attempts to revise legitimacy of actions, Charter authority, session suspension or conflict beyond agent/role mandate.
- Decisive decision or feedback right: Speaker/legitimate human authority determines constitutional rules or ruling on higher-authority matters, and the accepted decision returns to agent execution.
- Decision owner: Human `AUTHORITY` Speaker as legitimate parent of the governed session. Model workers may submit motions/Point of Order but cannot grant their own Assent or bypass suspension.
- Supporting / enforcement mechanisms: CHARTER.md validated at turn start, role/constituency checks, Speaker-only Assent/Ruling, STATE CONVENED/SUSPENDED, append-only Hansard and optional SCM projection.
- Closure path: Agent files a scope-overrun Point of Order → session SUSPENDED and notified → Speaker issues ruling/decision → state returned to CONVENED → next run re-reads Charter and ruling-rich Hansard/standing orders and is governed accordingly. Separately, carried identity/standing-order changes require human Assent and become authoritative recorded enacted decisions.
- Boundary reachability: `runTurn` rejects suspended sessions, reads `CHARTER.md`, injects Standing Orders and Hansard into agent prompt; `src/escalation.ts` implements authorized Speaker Ruling and return; `grantAssent` and CLI enforce named constitutional authority. The parent path is shipped even without hosted SCM.
- Why this is / is not agent-owned: The decisive ultimate-policy right stays with a human, not the model or deterministic gate. A real return-to-operation path distinguishes this parent S5 from mere prompt/static policy text.
- Evidence: https://github.com/cordfuse/politik/blob/c1fa7312c75599d72b187bf20088f51f5dda2247/src/charter.ts; https://github.com/cordfuse/politik/blob/c1fa7312c75599d72b187bf20088f51f5dda2247/src/runner.ts; https://github.com/cordfuse/politik/blob/c1fa7312c75599d72b187bf20088f51f5dda2247/src/escalation.ts; https://github.com/cordfuse/politik/blob/c1fa7312c75599d72b187bf20088f51f5dda2247/src/division.ts; https://github.com/cordfuse/politik/blob/c1fa7312c75599d72b187bf20088f51f5dda2247/src/cli.ts; https://github.com/cordfuse/politik/blob/c1fa7312c75599d72b187bf20088f51f5dda2247/src/state.ts
- Basis: explicit and structural.
- Confidence: moderate-high.
- Caveats: Only legitimate session-level constitutional decisions count. Ordinary per-motion task approvals or votes are not automatically S5; changing arbitrary real-world enterprise constitutions is not claimed..

- Identity / ultimate-policy issue: session Standing Orders, actor constitutional authority and escalated decisions that surpass the agent role's permitted action set.
- Ultimate authority in each claimed mode: shipped parent-governed mode only — named human Speaker with `AUTHORITY` role, subject to Charter/protocol rules.
- Return-to-operation path: ruling/assent recorded in session → authorized resumption or enacted Charter/standing-order context → subsequent `runTurn` reads state and Charter/Hansard and constrains next model turn.


## Distributed OSS parent arrangement

One local git session has a constitutional human Speaker; this source does not establish a durable federated organization of independent OSS contributors as a single operating recursion. Nested tree traversal and `registry` observe a local workspace hierarchy, not a separately constituted parent with distributed authority. Do not infer organization-wide parent modes from protocol archetypes, user prompts or repository co-location.

## Self-hosted and non-human modes

The CLI can run on a developer host/CI with a configured agent executable; a fully model-free session still supports deterministic governance and does not itself supply autonomous S1. Human Speaker authority is required in the documented reference (role `AUTHORITY` human-only); no non-human S5 mode is evidenced. External provider inference and optional GitHub projection supply computation and publication transport, respectively, not separate ultimate legitimacy.

## Recursion

One session may contain nested Org/Team/Sprint/Ticket directories with inherited Charters and local registry/cascade; these are addressable sub-sessions, not proven recursively viable autonomous agent organizations. Stateless one-turn workers are not automatically recursively viable S1 enterprises.

## Variety and escalation

Quorum thresholds, state suspension, per-turn cost ledger, escape-to-Speaker rulings and containment-after-execution distinguish governance risks. A POINT_OF_ORDER is an exceptional signal to the constitutional Speaker, not itself an S5/S3 capability; positive S5 depends on the actual human ruling and session return. The runner detects containment after the worker has already acted, so a model is not credibly sandboxed solely by its session Charter.

## Evidence gaps

- No live Claude/Codex/Gemini/OpenCode invocation was run by this assessment; it is a source-first review of wired execution.
- S2/S3 negatives are specific to a stateless governed session; stronger interpretation of cross-session operations needs first-party evidence of continuous units, concrete interference and whole-current regulation at this frozen ref.
- S3* bounded absence is about a complementary independent operational audit and management return, not whether Politik's immutable-intended Hansard and integrity detection are useful.
- S5=P credits Speaker-policy closure at the session recursion, not human assent over every routine motion as S5 or a deployed enterprise constitution.
- Optional GitHub provider merge applies only configured hosted session projections; no unverified real-world effect is borrowed.
