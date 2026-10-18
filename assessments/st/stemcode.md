---
harness_id: stemcode
project_name: StemCode
repository: https://github.com/rizwan3d/StemCode
review_ref: 8e52bb02310b91337bf6eb88e163fc65acb059f8
reviewed_at: 2026-09-30
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-09-30
status: proposed
autonomy_s1: A
autonomy_s2: A
autonomy_s3: —
autonomy_s3_star: C
autonomy_s4: —
autonomy_s5: —
---

# StemCode

## Review boundary

- System in focus: StemCode's first-party local coding-agent product at frozen revision `8e52bb02310b91337bf6eb88e163fc65acb059f8`, including the .NET conversation/tool runtime, built-in primary/subagent profiles, permission/session/file-edit machinery, supported CLI/Desktop/editor/headless surfaces, and shipped CI-review constructor/example surface where explicitly called out below.
- Purpose and identity: perform practical software-engineering work against a real repository while preserving local operator control, including repository inspection, planning, editing, validation, delegated investigation/implementation, review and automation-oriented execution.
- Relevant environment: user tasks, repository/worktree state, shell/build/test results, provider responses, external documentation/web results, LSP/code-intelligence results, configured workspace memory/instructions, permission decisions and PR/change-set evidence in the supported review surface.
- Standard-distribution boundary: StemCode's own conversation pipeline, built-in tools/profiles, subagent orchestration, permissions, sessions, tracked edits/undo and documented local execution surfaces are inside. External model providers, editors, language servers, web endpoints and hosting platforms are dependencies/interfaces. Workspace-authored profiles/memory can configure the runtime but do not donate unshipped organizational functions.
- Credited operating / distribution surfaces: `README.md`; `docs/documentation.md`; `StemCode/Application/Conversation/Services/AgentConversationPipeline.cs`; `StemCode/Application/Profiles/BuiltInAgentProfiles.cs`; `StemCode/Application/Tools/AgentDelegateTool.cs`; `StemCode/Application/Tools/AgentOrchestrateTool.cs`; `StemCode/Application/Tools/AgentDelegationSupport.cs`; permission/session/workspace-file services reachable from the supported CLI/Desktop/editor/headless runtime. For S3* constructor evidence only, the shipped `.github/stemcode-github-review.sh`, `.github/workflows/stemcode-review.yml` and `.stemcode/agents/pr-reviewer.md` surfaces are also inspected.
- Adjacent first-party surfaces excluded from ownership: repository-development workflows, release/signing/packaging CI, tests, contributor automation, example/config scaffolding not wired into an assessed run, and the StemCode project's own dogfood/governance activity. The shipped PR-review workflow is credited only as the narrow S3* constructor path described below; it does not donate S3/S4/S5 ownership to the ordinary coding runtime.
- First-party operating / deployment modes considered: interactive CLI; one-shot/headless CLI; Desktop/editor integrations backed by the same runtime; primary `build`, `plan`, and `review` profiles; delegated `general` and `explore` subagents; `agent_delegate`; `agent_orchestrate` with `auto`, `sequential`, and `parallel_readonly` strategies; permission-controlled local operation; shipped CI review constructor/example.
- Recursion level: the assessed organization is one primary StemCode session coordinating bounded child StemCode sessions. Child `general` and `explore` executions are distinct subordinate S1 units when invoked because each receives its own `ReplSessionContext`, model conversation pipeline and allowed tool surface while sharing the parent workspace. Their existence does not by itself establish full VSM recursion.
- Reviewed revision: `8e52bb02310b91337bf6eb88e163fc65acb059f8`.
- Observation date: 2026-09-30.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

StemCode's `AgentConversationPipeline` owns the ordinary model/tool execution cycle. A turn prepares the active profile/system prompt and tool definitions, invokes the provider, executes returned tools through first-party tool machinery, persists turn/session state, applies recovery/loop guards and continues until the turn completes or is interrupted. Built-in `build`, `plan` and `review` profiles change allowed tools and permission intent while using the same first-party runtime.

Delegation is first-party. `agent_delegate` creates a child `ReplSessionContext` with the same workspace/provider/model but a subagent profile, runs that child through the same `IConversationPipeline`, and returns the handoff plus executed-tool/edit evidence to the parent. `agent_orchestrate` accepts one to six focused child tasks. It can run read-only child tasks in parallel, while editing-capable child tasks are deliberately executed one at a time in `auto`; `parallel_readonly` rejects editing-capable subagents. The parent model chooses the task set, profiles, strategy and optional write scopes. Child prompts explicitly require bounded delegated scope, respect for other agents' changes and write-scope confinement when supplied.

StemCode also ships a dedicated PR-review constructor/example. The GitHub review script computes a base/head diff, invokes a separate read-only `pr-reviewer` StemCode profile, writes the review artifact and posts it as a PR review/comment. The committed workflow currently leaves `pull_request_target` commented out and therefore does not itself wire that reviewer into ordinary autonomous coding control; the path is nevertheless a first-party audit-specific construction surface.

Persistent repo memory and optional lesson memory are present, as are web search and codebase/LSP tools. They improve present and future task execution, but the reviewed boundary does not close an external-and-prospective S4 adaptation loop over StemCode's own organizational capability. Likewise permissions, profiles, workspace instructions and operator approval constrain operation without establishing runtime identity/ultimate-policy closure.

Primary evidence:

- [`README.md`](https://github.com/rizwan3d/StemCode/blob/8e52bb02310b91337bf6eb88e163fc65acb059f8/README.md)
- [`docs/documentation.md`](https://github.com/rizwan3d/StemCode/blob/8e52bb02310b91337bf6eb88e163fc65acb059f8/docs/documentation.md)
- [`StemCode/Application/Conversation/Services/AgentConversationPipeline.cs`](https://github.com/rizwan3d/StemCode/blob/8e52bb02310b91337bf6eb88e163fc65acb059f8/StemCode/Application/Conversation/Services/AgentConversationPipeline.cs)
- [`StemCode/Application/Profiles/BuiltInAgentProfiles.cs`](https://github.com/rizwan3d/StemCode/blob/8e52bb02310b91337bf6eb88e163fc65acb059f8/StemCode/Application/Profiles/BuiltInAgentProfiles.cs)
- [`StemCode/Application/Tools/AgentDelegateTool.cs`](https://github.com/rizwan3d/StemCode/blob/8e52bb02310b91337bf6eb88e163fc65acb059f8/StemCode/Application/Tools/AgentDelegateTool.cs)
- [`StemCode/Application/Tools/AgentOrchestrateTool.cs`](https://github.com/rizwan3d/StemCode/blob/8e52bb02310b91337bf6eb88e163fc65acb059f8/StemCode/Application/Tools/AgentOrchestrateTool.cs)
- [`StemCode/Application/Tools/AgentDelegationSupport.cs`](https://github.com/rizwan3d/StemCode/blob/8e52bb02310b91337bf6eb88e163fc65acb059f8/StemCode/Application/Tools/AgentDelegationSupport.cs)
- [`.github/stemcode-github-review.sh`](https://github.com/rizwan3d/StemCode/blob/8e52bb02310b91337bf6eb88e163fc65acb059f8/.github/stemcode-github-review.sh)
- [`.github/workflows/stemcode-review.yml`](https://github.com/rizwan3d/StemCode/blob/8e52bb02310b91337bf6eb88e163fc65acb059f8/.github/workflows/stemcode-review.yml)
- [`.stemcode/agents/pr-reviewer.md`](https://github.com/rizwan3d/StemCode/blob/8e52bb02310b91337bf6eb88e163fc65acb059f8/.stemcode/agents/pr-reviewer.md)

## Operational model

A primary StemCode actor receives the current engineering objective and autonomously selects repository/tool actions inside its active profile and permission envelope. Tool results return into the same conversation pipeline and can change the next action. For bounded side work, the primary actor can instantiate one child session or coordinate several child sessions. The orchestration tool exposes an explicit interference-control policy: read-only work may overlap, but editing-capable work is serialized, and the primary actor may further assign write scopes.

This supports an agent-owned S2 relation but not an S3 relation. The parent model does choose delegated work, yet `agent_orchestrate` is one bounded handoff call that waits for the requested group and returns aggregate results. The reviewed standard distribution does not expose a persistent whole-system current view over an independently evolving population of operational commitments plus intervention authority over that population.

## S1 — Operations

- State: A
- Function: perform repository-facing software-engineering work by interpreting the current objective, selecting permitted inspection/edit/shell/validation actions, executing them and revising subsequent actions from returned evidence.
- Disturbance / variety regulated: changing repository state, implementation alternatives, provider uncertainty, build/test/tool failures, incomplete plans, malformed/empty provider outputs and task-specific evidence discovered during execution.
- Decisive decision or feedback right: choose the next task-specific model/tool action and revise that choice after observing tool/provider/workspace evidence.
- Decision owner: the active model-backed StemCode primary actor; delegated child actors own the same local S1 discretion for their bounded task.
- Supporting / enforcement mechanisms: tool registry/execution pipeline, active profile, permission overlays, session persistence, provider adapters, plan/loop guards, workspace instructions/memory, tracked file-edit transactions and interrupt/recovery handling.
- Closure path: task/current session state → provider/model decision → first-party tool execution → result persisted and returned to the conversation → same actor selects another action or final response.
- Boundary reachability: the first-party `AgentConversationPipeline` and built-in profiles are the standard runtime used by the documented CLI/Desktop/editor/headless product surfaces; no adjacent development actor is required.
- Why this is / is not agent-owned: removing the model actor while retaining tools, permissions, sessions and deterministic guards removes the task-specific choice of what to inspect, edit, run or validate next; those mechanisms constrain or transport rather than replace that discretion.
- Evidence: [`AgentConversationPipeline.cs`](https://github.com/rizwan3d/StemCode/blob/8e52bb02310b91337bf6eb88e163fc65acb059f8/StemCode/Application/Conversation/Services/AgentConversationPipeline.cs); [`BuiltInAgentProfiles.cs`](https://github.com/rizwan3d/StemCode/blob/8e52bb02310b91337bf6eb88e163fc65acb059f8/StemCode/Application/Profiles/BuiltInAgentProfiles.cs); [`README.md`](https://github.com/rizwan3d/StemCode/blob/8e52bb02310b91337bf6eb88e163fc65acb059f8/README.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: particular tools may require operator approval or be denied by profile/policy, but supported operation retains autonomous task-level decision/action loops.

## S2 — Coordination

- State: A
- Function: attenuate destructive interference among subordinate S1 units when a primary StemCode actor coordinates several bounded child tasks against the same workspace.
- Disturbance / variety regulated: simultaneous editing-capable subagents could overwrite, revert or otherwise conflict with one another in the shared repository; unconstrained delegated scopes can also create cross-task churn.
- Distinct S1 units: separate child `ReplSessionContext` executions created by `agent_orchestrate`, each running the first-party conversation pipeline under `general` or `explore` and returning its own tool/output/edit evidence.
- Inter-S1 disturbance: editing-capable child actors share the parent workspace and can therefore contend on repository mutations; StemCode's own orchestration contract distinguishes these from read-only tasks and explicitly warns coordinated agents not to revert others' changes.
- Attenuating coordination relation: the primary model chooses the child task set, subagent profiles, execution strategy and optional write scopes; `auto` then parallelizes consecutive read-only tasks but executes editing-capable tasks in controlled sequence, while `parallel_readonly` rejects mutating subagents entirely. Delegated prompts transmit task/write-scope/coordination constraints to each S1.
- Feedback into subsequent S1 behaviour: strategy and write-scope choices alter when child S1s run and what workspace region they are instructed to touch; each child handoff/tool/edit result returns to the parent actor, which can integrate the evidence into subsequent operation or another coordinated handoff.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the relation is explicitly conditioned on the concrete interference class of shared-workspace mutations. Read-only work is allowed to overlap; editing-capable work is deliberately serialized or rejected from the parallel mode, and bounded write scopes are passed to mutating children. This is targeted disturbance attenuation, not sequencing merely because tasks exist.
- Decisive decision or feedback right: decide which bounded child activities should coexist, which agent profile should perform each, what coordination strategy to use and what write boundaries to assign before those S1s operate.
- Decision owner: the primary model-backed StemCode actor owns the task-specific coordination discretion; deterministic orchestration code enforces the nonparallel mutation safety rule and concurrency limit.
- Supporting / enforcement mechanisms: `AgentOrchestrateTool`; child-session construction; `MaxParallelReadOnlyTasks`; editing-capable classification; strategy validation; semaphore; sequential execution of mutating requests; delegated coordination/write-scope prompt; returned aggregate result.
- Closure path: primary actor identifies independent/dependent side work → calls `agent_orchestrate` with tasks/strategy/scopes → runtime schedules read-only parallelism and mutation serialization → child S1s receive coordination constraints and operate → their results/edit evidence return to the primary actor → later primary/child behaviour can be revised.
- Boundary reachability: `agent_orchestrate` is in the standard `build` profile and in supported inspection-oriented primary profiles where applicable; child `general`/`explore` profiles and the execution policy are shipped first-party runtime behavior.
- Why this is / is not agent-owned: if the primary actor is removed, deterministic code can still serialize a pre-existing request, but no task-specific actor remains to decide the coordinated task set, child profiles, strategy or write scopes. The runtime owns enforcement; the primary agent owns the bounded coordination choice.
- Evidence: [`AgentOrchestrateTool.cs`](https://github.com/rizwan3d/StemCode/blob/8e52bb02310b91337bf6eb88e163fc65acb059f8/StemCode/Application/Tools/AgentOrchestrateTool.cs); [`AgentDelegationSupport.cs`](https://github.com/rizwan3d/StemCode/blob/8e52bb02310b91337bf6eb88e163fc65acb059f8/StemCode/Application/Tools/AgentDelegationSupport.cs); [`BuiltInAgentProfiles.cs`](https://github.com/rizwan3d/StemCode/blob/8e52bb02310b91337bf6eb88e163fc65acb059f8/StemCode/Application/Profiles/BuiltInAgentProfiles.cs).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: this S2 is bounded to one orchestration handoff and the shared-workspace interference it regulates; it does not imply persistent organization-wide current control.

## S3 — Inside-and-now control

- State: —
- Function: no material first-party S3 whole-current control loop was established at the assessed recursion.
- Disturbance / variety regulated: task decomposition, active-plan tracking, permission enforcement, orchestration batch scheduling and token/budget limits exist, but no distinct whole-system current-operation variety is shown being regulated through S3 authority.
- Decisive decision or feedback right: not established.
- Decision owner: not established.
- Supporting / enforcement mechanisms: live plan/update-plan machinery, bounded subagent orchestration, permission profiles, budget controls, session state, interrupts and deterministic concurrency limits.
- Closure path: absent at S3 level; no first-party persistent whole-system current view → shared-resource/commitment/priority intervention → returned change to an independently evolving operational population was found.
- Why this is / is not agent-owned: the primary model does allocate bounded delegated work, but that is parent-task decomposition inside one awaited orchestration call. The reviewed path does not expose the whole-system current view and current-control authority required by the Profile.
- Evidence: [`AgentOrchestrateTool.cs`](https://github.com/rizwan3d/StemCode/blob/8e52bb02310b91337bf6eb88e163fc65acb059f8/StemCode/Application/Tools/AgentOrchestrateTool.cs); [`BuiltInAgentProfiles.cs`](https://github.com/rizwan3d/StemCode/blob/8e52bb02310b91337bf6eb88e163fc65acb059f8/StemCode/Application/Profiles/BuiltInAgentProfiles.cs); [`AgentConversationPipeline.cs`](https://github.com/rizwan3d/StemCode/blob/8e52bb02310b91337bf6eb88e163fc65acb059f8/StemCode/Application/Conversation/Services/AgentConversationPipeline.cs).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: future/background-task machinery could change this conclusion if it supplied a population view plus substantive intervention rights; that path is not established in the frozen revision.

### Absence scope

- Surfaces inspected: primary conversation/session runtime; live planning/recovery guards; `agent_delegate`; `agent_orchestrate`; built-in primary/subagent profiles; permission/budget/session mechanisms; README/documented CLI/Desktop/editor/headless surfaces.
- Plausible first-party paths checked: persistent subagent/task registries; background-worker lifecycle control; whole-system workload/status dashboards; dynamic resource/budget allocation; commitment cancellation/reprioritization; orchestration batch state; plan tracking as a possible current-control surface.
- Why no material first-party path remains: the first-party multi-agent path is an awaited bounded handoff without an independently evolving subordinate population or persistent whole-system view. Deterministic limits and plan state constrain one operational stream rather than closing S3 on behalf of the whole.

## S3* — Complementary audit

- State: C
- Function: provide an audit-specific, read-only review path over a proposed change set that is separate from the ordinary implementation actor and can challenge its claims with findings about bugs, regressions, unsafe assumptions, edge cases and missing tests.
- Disturbance / variety regulated: uncertainty that the normal implementation/reporting path may miss defects or weak tests in a PR/change set.
- Claim being audited: that a proposed repository change is correct/safe enough with no material unreported regressions or testing gaps.
- Ordinary reporting path: the ordinary coding actor edits/runs validation and reports completion through its primary session/tool loop; routine build/test results remain part of that production path.
- Complementary access path: shipped GitHub review automation computes the independent base/head diff, invokes a separate read-only `pr-reviewer` profile against that artifact and publishes findings as a PR review/comment, with an uploaded review artifact.
- Independence boundary: the reviewer is a separately invoked StemCode session/profile with read-only/safe-inspection permissions and receives the PR diff rather than inheriting the implementation actor's conversational claims. However the committed workflow's PR trigger is commented out and the path does not autonomously drive corrective execution back into the ordinary coding actor.
- Who acts on findings: the hosting-platform/user/developer workflow consuming the posted PR findings; first-party StemCode does not in this frozen standard setup automatically convert those findings into a corrective implementation turn.
- Decisive decision or feedback right: first-party tooling exposes the audit-specific independent judgment and outbound findings path, but the autonomous corrective authority/return closure must still be composed by the adopter.
- Decision owner: constructor state. StemCode supplies the independent model-backed reviewer and findings publication primitive; deployment wiring and downstream corrective authority remain outside the closed autonomous product loop.
- Supporting / enforcement mechanisms: `pr-reviewer` read-only profile; base/head diff construction; review script; GitHub workflow permissions/artifact upload; PR comment/review publication.
- Closure path: first-party path reaches PR findings publication but stops before autonomous corrective control; an adopter must compose the findings-consumer/repair return path for full closure.
- Boundary reachability: the audit path is explicitly shipped and documented as StemCode CI review automation with first-party scripts/profile/workflow, so the S3*-specific constructor is reachable without borrowing a third-party reviewer. The missing autonomous corrective return is why the state is `C`, not `A`.
- Why this is / is not agent-owned: the audit judgment itself is made by a separate model-backed reviewer, not by a deterministic parser. The incomplete part is organizational closure from findings back into corrective operation, so the assessment does not publish `A`.
- Evidence: [`.github/stemcode-github-review.sh`](https://github.com/rizwan3d/StemCode/blob/8e52bb02310b91337bf6eb88e163fc65acb059f8/.github/stemcode-github-review.sh); [`.github/workflows/stemcode-review.yml`](https://github.com/rizwan3d/StemCode/blob/8e52bb02310b91337bf6eb88e163fc65acb059f8/.github/workflows/stemcode-review.yml); [`.stemcode/agents/pr-reviewer.md`](https://github.com/rizwan3d/StemCode/blob/8e52bb02310b91337bf6eb88e163fc65acb059f8/.stemcode/agents/pr-reviewer.md); [`docs/documentation.md`](https://github.com/rizwan3d/StemCode/blob/8e52bb02310b91337bf6eb88e163fc65acb059f8/docs/documentation.md).
- Basis: explicit + structural.
- Confidence: medium-high.
- Caveats: repository co-location alone is not used as evidence. The positive state is intentionally only the shipped audit-specific constructor path; ordinary `review` profile use inside the same production conversation and routine tests are not credited as S3*.

## S4 — Outside-and-then intelligence

- State: —
- Function: no material first-party external-and-prospective adaptation loop over StemCode's own current capability was established.
- Disturbance / variety regulated: web search, codebase intelligence, repository/team memory and optional lessons expose useful information for task execution and reuse, but they do not establish S4 at the assessed organizational recursion.
- Decisive decision or feedback right: not established.
- Decision owner: not established.
- Supporting / enforcement mechanisms: `web_search`, headless browser, codebase/LSP tools, repo memory, lesson memory, automatic tool-failure observation, skills and configurable profiles/providers.
- Closure path: no external/future distinction → adaptation-option development → return into present organizational capability/S3 loop was established. Lesson retrieval returns prior local mistakes/fixes to future prompts but is not an external-and-prospective adaptation conversation.
- Why this is / is not agent-owned: the model can use web/repository evidence for the current task and can save/retrieve lessons, but that is current-task sensing/learning unless tied to future-oriented organizational adaptation of capability.
- Evidence: [`BuiltInAgentProfiles.cs`](https://github.com/rizwan3d/StemCode/blob/8e52bb02310b91337bf6eb88e163fc65acb059f8/StemCode/Application/Profiles/BuiltInAgentProfiles.cs); [`StemCode/Application/Tools/LessonMemoryTool.cs`](https://github.com/rizwan3d/StemCode/blob/8e52bb02310b91337bf6eb88e163fc65acb059f8/StemCode/Application/Tools/LessonMemoryTool.cs); [`docs/documentation.md`](https://github.com/rizwan3d/StemCode/blob/8e52bb02310b91337bf6eb88e163fc65acb059f8/docs/documentation.md).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: future support for agent-owned capability/profile/tool adaptation driven by environmental/future modeling could establish S4; current reusable memory alone does not.

### Absence scope

- Surfaces inspected: web/browser tools; codebase/LSP intelligence; workspace/repo memory; lesson-memory save/search/edit/retrieval and automatic failure observation; skills/profiles/providers; planning and review modes; documented automation surfaces.
- Plausible first-party paths checked: environmental monitoring; model/tool/provider capability discovery; future-scenario generation; adaptation-option evaluation; automated profile/tool/skill reconfiguration; lessons as prospective adaptation; external documentation lookup as possible S4 sensing.
- Why no material first-party path remains: reviewed external sensing is invoked for current engineering tasks, while persistent lessons encode local mistakes/fixes for reuse. Neither is coupled to a first-party prospective adaptation decision that changes StemCode's present organizational capability.

## S5 — Policy and identity

- State: —
- Function: no material first-party runtime identity/ultimate-policy closure was established at the assessed recursion.
- Disturbance / variety regulated: permissions, profiles, workspace instructions, budgets, approval prompts and operator configuration constrain ordinary operation, but no S5-level identity/policy issue is adjudicated through a runtime ultimate-authority loop.
- Decisive decision or feedback right: not established for identity/ultimate policy.
- Decision owner: not established at S5; developers/operators author configuration and ordinary approval choices outside any qualifying first-party S5 closure.
- Supporting / enforcement mechanisms: built-in profile permission overlays; allow/deny/ask rules; workspace files/instructions; provider/model configuration; budget controls; operator prompts and runtime enforcement.
- Closure path: absent at S5 level; no identity/ultimate-policy issue → legitimate ultimate authority → authoritative decision → returned policy governing subsequent operation path was found in the standard distribution.
- Why this is / is not agent-owned: the model is constrained by configured policy but does not own the ultimate right to redefine StemCode's identity or top-level policy; static configuration and ordinary tool approval are specifically insufficient for S5.
- Evidence: [`BuiltInAgentProfiles.cs`](https://github.com/rizwan3d/StemCode/blob/8e52bb02310b91337bf6eb88e163fc65acb059f8/StemCode/Application/Profiles/BuiltInAgentProfiles.cs); [`README.md`](https://github.com/rizwan3d/StemCode/blob/8e52bb02310b91337bf6eb88e163fc65acb059f8/README.md); [`docs/documentation.md`](https://github.com/rizwan3d/StemCode/blob/8e52bb02310b91337bf6eb88e163fc65acb059f8/docs/documentation.md).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: repository maintainer governance is adjacent to the product boundary and is not imported as runtime S5 merely because it determines future releases.

### Absence scope

- Surfaces inspected: built-in profiles; permission overlays/rules; workspace instructions/configuration; budget controls; provider/model selection; approval prompts; CI/release/governance adjacency; documented operator controls.
- Plausible first-party paths checked: runtime constitutional/identity decisions; autonomous policy revision; parent escalation of identity-level disputes; durable ultimate-policy decisions returning into the running harness; maintainer/release governance as a possible distributed parent path.
- Why no material first-party path remains: the inspected product surfaces enforce developer/operator-authored constraints and ordinary approvals. Adjacent repository governance changes future artifacts rather than supplying a boundary-reachable runtime identity/ultimate-policy closure for the assessed product.

## Recursion

StemCode can create child sessions that are locally autonomous S1 units for bounded delegated work. They have a local task, workspace environment, model/tool loop and profile constraints, and their results return to the primary actor. The review did not establish that each child also contains the metasystemic functions needed to classify it as a recursively viable system; therefore spawning child sessions is recorded as operational nesting rather than a separate full VSM recursion claim.

## Variety and escalation

StemCode attenuates operational variety through active profiles, permission rules, bounded orchestration, context/session persistence, plan/loop guards and deterministic mutation-serialization in multi-subagent work. It amplifies capability through repository search, code intelligence, shell/build/test tools, web access, delegated child contexts and review surfaces. Operator approval can stop or permit particular tool actions, but ordinary approval is not promoted to S5.

The most material escalation boundary is from a child S1 back to the primary actor: each delegated result reports response, executed tools and tracked edits, allowing the primary actor to integrate evidence or choose a different next step. The separate CI-review constructor publishes audit findings outward but does not by itself close corrective control back into the coding actor.

## Evidence gaps

- The frozen revision does not demonstrate an autonomous consumer that turns CI `pr-reviewer` findings into corrective coding turns; this is the main reason S3* is `C` rather than `A`.
- No persistent whole-current subordinate population/control surface was found for S3 beyond one awaited orchestration batch.
- No first-party external/prospective capability-adaptation loop was found for S4; lesson memory is intentionally not treated as sufficient.
- No runtime identity/ultimate-policy closure was found for S5.
