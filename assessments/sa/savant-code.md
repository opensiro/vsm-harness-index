---
harness_id: savant-code
project_name: Savant-Code
repository: https://github.com/savant0x/savant-code
review_ref: dbe8b40559e7a455db21b904e512f96b454bdab3
reviewed_at: 2026-10-26
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: A
autonomy_s2: C
autonomy_s3: A
autonomy_s3_star: A
autonomy_s4: P
autonomy_s5: —
---

# Savant-Code

## Review boundary

- System in focus: The shipped Bun/TypeScript Savant-Code terminal assistant's first-party model/tool loop, specialist-agent composition, ECHO phase/evidence enforcement, optional FID worktree lanes, and locally governed skill-improvement route.
- Purpose and identity: Perform software engineering tasks through model-directed tools while retaining role-separated review, durable FID evidence and operator-controlled changes to reusable skills.
- Relevant environment: Local source repository, filesystem and Git, Bun runtime, configured local Ollama/hosted inference providers, tools/MCP/search resources, user terminal and optional evaluation commands.
- Standard-distribution boundary: Installed `savant-code` CLI with `cli`, `packages/agent-runtime`, `agents`, `common`, first-party ECHO gates and self-improving-harness commands. Supported `HYBRID`, `STRICT`, `ANALYZE`, optional FID worktree and skill trust modes considered individually. Model serving and user-run tool environments remain dependencies.
- Credited operating / distribution surfaces: CLI mode/commands, `packages/agent-runtime/src/{run-agent-step,tools/handlers,echo,provenance}`, shipped `agents/{savant,verifier,adversary,forge,detective,recorder}`, `common/src/util/skill-management`, `scripts/{session-end-review,lessons-to-skills,evolve-skills}.ts`, `cli/src/commands/skills.ts`, the bundled ECHO role and policy prompts.
- Adjacent first-party surfaces excluded from ownership: Maintainer CI/release procedures, static ECHO prose taken alone, declared-only `protocol.config.yaml` orchestration-preset event graph (not a runner), standalone evals/benchmark scores and teaching demo, optional remote Savant backend, external LLM provider policies and native test fixtures.
- First-party operating / deployment modes considered: Standard HYBRID main agent with direct tools and bounded escalation; STRICT multi-role FID ceremony and fresh Verifier/Adversary; operator-selected ANALYZE read-only mode; optional `fid_worktree` per-FID parallel lanes; session-end experience capture, skill draft quarantine and operator `/skills trust`.
- Recursion level: One user-owned local Savant coding workspace and its coordinated agent sessions; optional multiple concurrent FID execution lanes at the same repository recursion; skill governance at the workspace parent operator boundary.
- Reviewed revision: `dbe8b40559e7a455db21b904e512f96b454bdab3`.
- Observation date: 2026-10-26.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

The CLI instantiates model-backed main and specialist agent templates from first-party `agents/` definitions. `run-agent-step` calls the selected provider, dispatches model-chosen tools through the first-party tool executor, appends outcomes and repeats until completion, cancellation or policy/budget exit. The shipped tool handler table routes `spawn_agents` and `spawn_agent_inline` through authenticated agent selection and per-role tool lists. In `HYBRID`, the main Savant agent may edit code directly under write gates and escalate significant work. In `STRICT`, the role prompts require Detective/Forge/Verifier/Adversary and FID evidence; code implements phase gates and review/provenance bindings. The `protocol.config.yaml` `orchestration` event preset is a validation declaration, not an executable separate event scheduler, and is not credited by itself.

`EHEL` pre-write gates handle read-before-write, approval/scope and verification constraints; FID phase validation, post-write scans and outcome receipts are supporting enforcement. The Verifier has an empty tool set and receives raw evidence injected by the harness; the Adversary is a distinct read-only agent with direct source-search tools that re-checks citations and can overturn findings. Optional FID worktrees use a host-owned cross-process lock, isolated lanes and a refusal-only merge check. A separate experience/skills lifecycle captures recurring tool failures and forms quarantined skill draft proposals; the live skill loader excludes them until the user invokes the trust command with the required review/trigger-case evidence. This last route is parent-governed prospective adaptation, not silent autonomous evolution.

Primary source: [main README / supported modes](https://github.com/savant0x/savant-code/blob/dbe8b40559e7a455db21b904e512f96b454bdab3/README.md), [runtime model/tool loop](https://github.com/savant0x/savant-code/blob/dbe8b40559e7a455db21b904e512f96b454bdab3/packages/agent-runtime/src/run-agent-step.ts), [tool handler registry](https://github.com/savant0x/savant-code/blob/dbe8b40559e7a455db21b904e512f96b454bdab3/packages/agent-runtime/src/tools/handlers/list.ts), [ECHO role contract](https://github.com/savant0x/savant-code/blob/dbe8b40559e7a455db21b904e512f96b454bdab3/ECHO.md).

## Operational model

The main Savant coding model and delegated specialist instances are task-operating S1 units. The main model also owns real-time work direction at one workspace/task scope, while the code's hard gates enforce existing constraints rather than independently choosing project priorities. The Verifier/Adversary audit pair is complementary to ordinary implementation reporting and independently challenges claims with raw source evidence; its feedback returns to task correction. Optional parallel FID lanes prevent writes and merge attempts from interfering but supply no autonomous conflict arbitrator. The skills lifecycle considers cross-session failure trends and prospective capability drafts, with the human operator retaining release authority and a concrete return to the live skill loader. Written laws and user consent alone do not show an ultimate identity-level adjudication loop.

## S1 — Operations

- State: A
- Function: Implement user-scoped coding tasks by choosing source inspections, edits, commands and subsequent steps in response to tool feedback.
- Disturbance / variety regulated: Changed source files, unknown code paths, build and test failures, tool errors, model responses and requested task changes.
- Decisive decision or feedback right: The main or delegated model selects tools and arguments for its task, observes executed results and chooses next actions or final output.
- Decision owner: Model-backed Savant main agent (HYBRID) and routed specialist models (STRICT/delegations) instantiated by the shipped agent runner.
- Supporting / enforcement mechanisms: Tool registry, filesystem safeguards, model adapters, context buffers, evidence ledger, `end_turn` gate and optional FID enforcement.
- Closure path: User goal/current messages → model request → first-party tool execution → response/result and repository feedback → updated model message/history and subsequent action.
- Boundary reachability: The published CLI enters `run-agent-step` and executable tool handlers with first-party agent templates; installed model providers supply tokens but do not replace the first-party tool/action feedback path.
- Why this is / is not agent-owned: The agent chooses task-specific operations; EHEL validates and blocks prohibited effects rather than generating those implementation decisions.
- Evidence: [run-agent-step and loop](https://github.com/savant0x/savant-code/blob/dbe8b40559e7a455db21b904e512f96b454bdab3/packages/agent-runtime/src/run-agent-step.ts), [tool dispatcher](https://github.com/savant0x/savant-code/blob/dbe8b40559e7a455db21b904e512f96b454bdab3/packages/agent-runtime/src/tools/handlers/list.ts), [README runtime contract](https://github.com/savant0x/savant-code/blob/dbe8b40559e7a455db21b904e512f96b454bdab3/README.md).
- Basis: first-party model/tool code and documented shipped entrypoints.
- Confidence: high.
- Caveats: Provider account/weights, actual coding accuracy and live LLM outcomes were not tested.

## S2 — Coordination

- State: C
- Function: Attenuate concrete interference among multiple FID task lanes working from one source repository.
- Disturbance / variety regulated: Independent task worktrees could mutate the same checkout, cross-use code graph state or merge incompatible/stale changes into main.
- Decisive decision or feedback right: The host creates registered isolated FID worktrees and refuses stale, dirty, nonconverged, conflicting or wrong-branch merges; no autonomous agent owns merge-conflict resolution across the teams.
- Decision owner: First-party deterministic FID worktree lifecycle/merge primitive under operator/model-issued action; developer/operator chooses how to resolve a refused merge.
- Supporting / enforcement mechanisms: Cross-process lock, per-FID branch/worktree record, Git `merge-tree` dry-run, exact base SHA, clean-tree checks, graph snapshot/refresh and refusal reasons.
- Closure path: Concurrent FID teams → distinct managed repository lanes → specialized operations on lane-specific source → attempted merge checked against main and either fast-forwarded or explicitly refused with conflict/divergence feedback → operator/team must adjust before subsequent write/integration.
- Boundary reachability: The shipped `fid_worktree` host tool routes create/merge/list/dispose through `runFidWorktreeAction` and `mergeFidWorktree`; it is an optional supported workspace mode, not a test-only helper.
- Why this is / is not agent-owned: It is a first-party function-specific inter-team interference barrier and feedback path (`C`); deterministic refusal and human/model repair after a conflict do not constitute autonomous S2 arbitration (`A`).
- Distinct S1 units: Two or more FID coding-agent sessions operating in parallel lane worktrees, each making coding decisions for its assigned FID.
- Inter-S1 disturbance: Cross-team shared-filesystem writes and incompatible lane changes reaching a common main or graph state.
- Attenuating coordination relation: Registered lane identities, cross-process lifecycle lock, protected base/ref checks, conflict-only refusal and independent worktree environments.
- Feedback into subsequent S1 behaviour: A denied merge identifies the exact blocked condition; the lane remains isolated while an operator or coding agent repairs/rebases instead of silently contaminating main.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: The worktree and merge guard explicitly prevent cross-S1 modification/commit interference; mere task delegation or ECHO phase order is not treated as S2.
- Evidence: [FID worktree service](https://github.com/savant0x/savant-code/blob/dbe8b40559e7a455db21b904e512f96b454bdab3/packages/agent-runtime/src/echo/parallel/fid-worktree-service.ts), [refusal-only merge](https://github.com/savant0x/savant-code/blob/dbe8b40559e7a455db21b904e512f96b454bdab3/packages/agent-runtime/src/echo/parallel/fid-worktree-merge.ts), [merge tests](https://github.com/savant0x/savant-code/blob/dbe8b40559e7a455db21b904e512f96b454bdab3/packages/agent-runtime/src/__tests__/fid-worktree-merge.test.ts).
- Basis: explicit function-specific optional runtime and targeted test sources.
- Confidence: medium-high.
- Caveats: Conflict resolution is explicitly *not* automated. No S2 claim is drawn from deterministic ECHO phase handoffs among roles of one task.

## S3 — Inside-and-now control

- State: A
- Function: Maintain task-wide present coordination over active coding/review specialists and required evidence/quality commitments.
- Disturbance / variety regulated: Unresolved task scope, competing immediate implementation priorities, failed review, incomplete FID evidence and blocked phase transitions.
- Decisive decision or feedback right: The main orchestrating model chooses coding strategy, whether to write directly or delegate, which specialist to call, what follow-up to request from review, and when to request completion; guards may reject the proposed decision.
- Decision owner: First-party main Savant Orchestrator model with specialist routing capabilities; phase/evidence engines are transport and constraints.
- Supporting / enforcement mechanisms: Agent definitions, allowed tool/spawn lists, FID phase gates, EHEL write/refusal checks, outcome messages, Auto Drive phase directives and loop guards.
- Closure path: Task goal and live tool/FID evidence → Orchestrator model's decomposition/delegation/correction → specialist operations and adversarial verdicts → updated work/current commitments or completion.
- Boundary reachability: The shipped model/tool runtime registers `spawn_agents` and `spawn_agent_inline` and supplies an actual Orchestrator prompt/role; the optional STRICT role chain is explicitly selectable, while the declared-only event orchestration preset contributes no extra owner.
- Why this is / is not agent-owned: The LLM chooses real work priorities, handoffs and responses to findings; deterministic strict gates constrain legality and protect evidence rather than deciding substantive work strategy.
- Whole-system current view: Current user goal, conversation, selected execution mode, tool state/results, active FID and role phase, returned reports, audit findings and context/evidence state for the local task team.
- Current-control decision scope: Task decomposition, delegated work and reviewer feedback, immediate repair/re-analysis/closure commitments; not across all unrelated installed Savant user workspaces.
- Evidence: [main runtime step](https://github.com/savant0x/savant-code/blob/dbe8b40559e7a455db21b904e512f96b454bdab3/packages/agent-runtime/src/run-agent-step.ts), [spawn handler](https://github.com/savant0x/savant-code/blob/dbe8b40559e7a455db21b904e512f96b454bdab3/packages/agent-runtime/src/tools/handlers/tool/spawn-agents.ts), [phase driver](https://github.com/savant0x/savant-code/blob/dbe8b40559e7a455db21b904e512f96b454bdab3/packages/agent-runtime/src/run-agent-step/auto-drive-driver.ts), [README HYBRID/STRICT](https://github.com/savant0x/savant-code/blob/dbe8b40559e7a455db21b904e512f96b454bdab3/README.md).
- Basis: first-party runtime model authority plus bounded phase-return contract.
- Confidence: medium-high.
- Caveats: A generic static event preset in `protocol.config.yaml` is declaration-only. Auto Drive deterministic FID selection does not itself own agentic S3 judgment.

## S3* — Complementary audit

- State: A
- Function: Challenge code-change and ordinary implementer/Verifier quality claims with independently observed evidence and return actionable findings into current work.
- Disturbance / variety regulated: Unsupported success reports, fabricated or stale line citations, missed high-risk checks and self-review blindness.
- Decisive decision or feedback right: A fresh Verifier model renders evidence-bounded `PASS/FAIL/NEEDS-REVIEW` findings, while a separately spawned Adversary model independently resolves sources and may override Verifier findings; both findings are bound and returned to the task control/FID phase.
- Decision owner: Distinct first-party Verifier and Adversary agent roles backed by model calls; the Adversary's contradictory judgment is specifically a complementary audit rather than an inline deterministic permission gate.
- Supporting / enforcement mechanisms: Verifier zero-tool restriction, raw-evidence injection, Adversary read/search-only tools, `spawn_agent_inline`/`spawn_agents` verdict capture, FID phase validation, optional signed provenance bindings and mandatory no-write permission boundaries.
- Closure path: Forge/main change and claimed test/grep evidence → fresh Verifier independently assesses provided raw context → Adversary reads real source to re-check and can refute/confirm → verdict attached to task/FID review context → Orchestrator revises work/phase or records unresolved `NEEDS-REVIEW`.
- Boundary reachability: `agents/verifier/verifier.ts` and `agents/adversary/adversary.ts` are shipped named agent definitions; live spawn handlers parse their verdicts and the STRICT mode contracts request both roles after implementation. This does not rely on offline benchmark judges.
- Why this is / is not agent-owned: The auditor models choose which claims pass or fail and the fresh Adversary has its own source-evidence search right; deterministic binding and evidence adapters enforce that output but do not predetermine the verdict.
- Claim being audited: Code change meets the converged FID/user requirements, the tests/checks actually ran, and cited source bytes support implementer and Verifier claims.
- Ordinary reporting path: Forge/main agent change summary and its tool outputs return to Orchestrator.
- Complementary access path: Verifier receives raw change/test/graph evidence outside ordinary reports; Adversary independently opens source and call sites with read-only tools to test Verifier citations.
- Independence boundary: New specialist model invocations have distinct agent templates/tools and cannot write; Verifier is zero-tool, Adversary's independent reads are not the implementing agent's own self-report. Optional ZTAP receipts attest role separation mechanically, not epistemic truth.
- Who acts on findings: The main Orchestrator via current rework/phase choice and FID evidence gates.
- Evidence: [Verifier role](https://github.com/savant0x/savant-code/blob/dbe8b40559e7a455db21b904e512f96b454bdab3/agents/verifier/verifier.ts), [Adversary role](https://github.com/savant0x/savant-code/blob/dbe8b40559e7a455db21b904e512f96b454bdab3/agents/adversary/adversary.ts), [spawn verdict binding](https://github.com/savant0x/savant-code/blob/dbe8b40559e7a455db21b904e512f96b454bdab3/packages/agent-runtime/src/tools/handlers/tool/spawn-agent-inline-verdict.ts), [provenance verdict](https://github.com/savant0x/savant-code/blob/dbe8b40559e7a455db21b904e512f96b454bdab3/packages/agent-runtime/src/provenance/verdict.ts).
- Basis: distinct shipped role contracts, source-evidence tools and live verdict return.
- Confidence: medium-high.
- Caveats: This is a supported strict-mode autonomous audit, not proof every HYBRID file edit always invokes the pair; agent review accuracy was not empirically measured.

## S4 — Outside-and-then intelligence

- State: P
- Function: Use cross-session operational failures to propose and selectively adopt future tool-use/recovery skills for later coding-agent work.
- Disturbance / variety regulated: Repeated failure classes and erosion of skill utility observed across sessions; unreviewed skill drafts can degrade future operations.
- Decisive decision or feedback right: Mechanical recurrence and Scribe/skill authoring generate candidates, but **the human workspace operator alone** makes the live-skill trust/reject/rollback judgment; quarantined output is not available to active agents without that decision.
- Decision owner: Legitimate local parent operator through the shipped `/skills show <name> --review` and `/skills trust <name>` CLI workflow (and related untrust/rollback); autonomous models may propose but cannot authorize release.
- Supporting / enforcement mechanisms: `PostToolUseFailure` capture, cross-session dedup/14-day threshold, SessionEnd agenda, lesson-to-skill drafting, isolated skill-proposal quarantine and lifecycle ledger, version/diff/trigger-case gates and live skill loader exclusion.
- Closure path: Tool failure traces across sessions → repeated pattern / durable lesson candidate → quarantined skill draft → operator inspects exact draft and required trigger cases → operator `trustSkill` promotes to canonical live skill → next agent session can discover/load new skill, altering usable present capability.
- Boundary reachability: `protocol.config.yaml` declares the first-party failure/SessionEnd hooks; published Bun scripts generate proposals, the CLI dispatches the actual operator-only trust route into `trustSkill`, and skill loader excludes drafts until it is run.
- Why this is / is not agent-owned: This is a closed **parent-governed** adaptation mode (`P`). Autonomous draft generation is not autonomous S4 ownership because no agent has the decisive promotion right; a one-click full automatic adaptation path is not claimed.
- External distinction: Changes in observed tool/provider/workspace failure signatures across different previous coding sessions, represented as classified and deduplicated experience records.
- Future / prospective distinction: A recovery technique to be available for similar future failures, subject to the existing live-skill baseline and regression/trigger-case review.
- Adaptation option generated: Proposed `SKILL.md` draft or revision/FID from recurrent tool failures, held in quarantine.
- Path back into current capability / S3: Operator trust changes the canonical `.agents/skills/<name>/SKILL.md` accessible to later `skill` loading and hence the Orchestrator's future task capability.
- Evidence: [self-improving harness guide](https://github.com/savant0x/savant-code/blob/dbe8b40559e7a455db21b904e512f96b454bdab3/docs/self-improving-harness.md), [SessionEnd capture/review](https://github.com/savant0x/savant-code/blob/dbe8b40559e7a455db21b904e512f96b454bdab3/scripts/session-end-review.ts), [lesson candidate/draft](https://github.com/savant0x/savant-code/blob/dbe8b40559e7a455db21b904e512f96b454bdab3/scripts/lessons-to-skills.ts), [CLI trust decision](https://github.com/savant0x/savant-code/blob/dbe8b40559e7a455db21b904e512f96b454bdab3/cli/src/commands/skills.ts), [live trust transition](https://github.com/savant0x/savant-code/blob/dbe8b40559e7a455db21b904e512f96b454bdab3/common/src/util/skill-management/trust.ts), [loader guard](https://github.com/savant0x/savant-code/blob/dbe8b40559e7a455db21b904e512f96b454bdab3/packages/agent-runtime/src/tools/handlers/tool/skill.ts).
- Basis: concrete parent decision and shipped capability return with independent historical signal and draft construction.
- Confidence: medium.
- Caveats: `lessons:to-skills` and `skills:evolve` are invoked as documented commands, not guaranteed on every SessionEnd. `skills:evolve` only creates proposals and does not touch live skills; the trust path requires valid skill trigger cases and explicit operator action. No runtime evidence of a successful real-world adaptation was collected.

## S5 — Policy and identity

- State: —
- Function: No complete identity/ultimate-policy issue-to-legitimate-authority-to-governing-return loop in the local assessed organization.
- Disturbance / variety regulated: ECHO process violations and risky commands threaten operational safety; that is not sufficient evidence for a constitutional identity dispute.
- Decisive decision or feedback right: No first-party S5-specific organizational purpose or ultimate identity judgment is wired into task execution.
- Decision owner: Not established at this recursion. Operator controls trust, model and mode settings, but those are operational/adaptation decisions, not shown to be S5 governance.
- Supporting / enforcement mechanisms: Static 15 ECHO laws, user approvals, EHEL enforcement and break-glass flags, model/provider selection and skill immutability.
- Closure path: Approval or mode changes can affect task rights, but no evidenced higher-level identity/policy issue → parent constitutional decision → changed organizational charter/current action path is supplied.
- Why this is / is not agent-owned: Fixed engineering policy and role prompts are design constraints, not a live agent or parent identity adjudicator.
- Evidence: [ECHO protocol document](https://github.com/savant0x/savant-code/blob/dbe8b40559e7a455db21b904e512f96b454bdab3/ECHO.md), [EHEL enforcement](https://github.com/savant0x/savant-code/blob/dbe8b40559e7a455db21b904e512f96b454bdab3/packages/agent-runtime/src/echo/enforcement.ts), [runtime config](https://github.com/savant0x/savant-code/blob/dbe8b40559e7a455db21b904e512f96b454bdab3/protocol.config.yaml).
- Basis: bounded structural negative.
- Confidence: medium.
- Caveats: The broader OSS project has maintainer governance, but a written constitution or user-facing risk approval alone does not demonstrate function-specific S5 closure at the local workspace boundary.

### Absence scope

- Surfaces inspected: ECHO laws, tool authorization and write gates, operator commands/modes, skill trust, FID evidence/provenance, remote provider and maintainer/release boundaries.
- Plausible first-party paths checked: ECHO identity language, user emergency override, skill promotion, strict/hybrid mode switches and public project governance.
- Why no material first-party path remains: These are immediate work authorization or parent-governed future capability control, and no shipped identity-level dispute plus authoritative decision-return loop is evidenced for the declared workspace organization.

## Distributed OSS parent arrangement

Repository contributors, maintainers and users can revise the open-source implementation, but their mere existence is not credited as a shared parent S3/S4/S5 function. The specific workspace operator has an evidenced S4 parent-adaptation authority; no project-wide governing parent claim is inferred.

## Self-hosted and non-human organizational boundary

Inference may be local (Ollama) or hosted, with first-party tools and governance around model actions. Local installation does not make external model architecture first-party. The autonomous S1/S3/S3* and parent-governed S4 ownership modes are distinct and need not be simultaneously exercised in every UI execution mode.

## Evidence gaps and reproducibility

- Frozen `dbe8b40559e7a455db21b904e512f96b454bdab3` was checked out and source-path/revision matched. No model/provider/agent-quality test was run.
- Bun runtime was unavailable in the assessment environment (`bun: command not found`); therefore the source's Bun/TypeScript unit/integration tests were **not run**, and no success is invented. Static inspection used first-party runtime, handlers, test sources and CLI/role contracts.
- The `protocol.config.yaml` declared orchestration event preset explicitly has no runner and is excluded from positive function attribution; actual role spawns and ECHO guards are separate live code.
- S2 is bounded to optional conflict-avoiding FID worktrees, S3* to supported review mode, and S4 to operator-approved trusted skills with required validation artifacts. These are organizational ownership claims, not evidence of LLM output quality.
