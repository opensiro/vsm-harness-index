---
harness_id: thread
project_name: thread
repository: https://github.com/Phytonking/thread
review_ref: b5516679c749da4410feda7c6b4b3cc67f4b4f06
reviewed_at: 2026-11-28
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.8
profile_version: 0.2.4
assessment_procedure_version: 0.3.8
status: included
autonomy_s1: A
autonomy_s2: A
autonomy_s3: A(P)
autonomy_s3_star: —
autonomy_s4: A
autonomy_s5: —
---

# thread

## Review boundary

- System in focus: One repository-local thread runtime, with main and its background workers.
- Purpose and identity: Carry out coding work through model-directed tools and parallel specialist threads.
- Relevant environment: Repository and worktree state, user requests and steering, configured model or CLI providers.
- Standard-distribution boundary: Installed Rust binary, local SQLite store, built-in tools and standard provider adapters.
- Credited operating / distribution surfaces: Native conversation loop, thread supervisor, worktrees, terminal controls and consolidation.
- Adjacent first-party surfaces excluded from ownership: BDD mock providers and tests, upstream provider internals and the maintainer project.
- First-party operating / deployment modes considered: Interactive REPL and native/provider-CLI workers. Worktree mode requires a Git project.
- Recursion level: One thread instance coordinating distinct coding operations.
- Reviewed revision: b5516679c749da4410feda7c6b4b3cc67f4b4f06
- Observation date: 2026-11-28
- Generated Profile version: 0.2.4
- Generated Methodology version: 0.3.8
- Current Profile version: 0.2.4
- Current Methodology version: 0.3.8

## Repository architecture

A terminal UI focuses a thread. The supervisor starts or resumes worker loops and relays inbox traffic. Workers persist state, tool events and completed handoffs in a repository-local database. Provider adapters support local models and authorized external CLIs. The same distribution runs later-context consolidation.

## Operational model

Main can perform work directly or allocate it to autonomous background units. Both use model-driven operations. A worktree-owning thread returns a report and branch, and main can read progress, steer or stop the worker. The operator can see the current roster and intervene in the REPL.

## S1 — Operations

- State: A
- Function: Complete a user request or bounded coding assignment.
- Disturbance / variety regulated: Uncertain repository state, failures and new input.
- Decisive decision or feedback right: Choose tools, respond to results and close the assignment.
- Decision owner: The model in main or a first-party background thread.
- Supporting / enforcement mechanisms: Built-in tool dispatcher, event state and provider selection.
- Closure path: Tool results enter the same conversation. The completed background report enters main's inbox.
- Why this is / is not agent-owned: The built-in loop owns the action-and-observation cycle.
- Boundary reachability: A supported native model mode calls the repository's own dispatcher directly.
- Evidence: [src/agent.rs](https://github.com/Phytonking/thread/blob/b5516679c749da4410feda7c6b4b3cc67f4b4f06/src/agent.rs#L408-L507), [src/runtime.rs](https://github.com/Phytonking/thread/blob/b5516679c749da4410feda7c6b4b3cc67f4b4f06/src/runtime.rs#L613-L651), [src/tools.rs](https://github.com/Phytonking/thread/blob/b5516679c749da4410feda7c6b4b3cc67f4b4f06/src/tools.rs#L126-L156)
- Basis: Static inspection of pinned first-party source.
- Confidence: high
- Caveats: The provider-CLI path delegates inference and some execution to configured providers.

## S2 — Coordination

- State: A
- Function: Prevent concurrent edits from interfering in the same working copy.
- Disturbance / variety regulated: Independent workers and main can overwrite or invalidate changes to the same checkout.
- Decisive decision or feedback right: Decide which coding assignment takes an isolated worktree and communicate its operating scope.
- Decision owner: Main's model.
- Supporting / enforcement mechanisms: Shipped worktree selection prompt, Git worktree creation and child context.
- Closure path: The worker starts in its worktree with a branch-specific mandate. Main receives its branch and result for subsequent integration.
- Why this is / is not agent-owned: The agent recognizes mutating work and selects isolation. Git supplies the actual separation.
- Boundary reachability: Main receives the shipped worktree policy and spawn tool, and the child launches from its assigned directory.
- Distinct S1 units: Main and independently running background coding threads, or two such background threads.
- Inter-S1 disturbance: Simultaneous edits may collide in the same checkout.
- Attenuating coordination relation: Main assigns separate writable working copies when granting an editing mandate.
- Feedback into subsequent S1 behaviour: The chosen directory and branch constrain where the new worker acts. Its resulting branch returns with the report.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: The native assignment guidance and mechanism explicitly address interference between simultaneous writers.
- Evidence: [src/agent.rs](https://github.com/Phytonking/thread/blob/b5516679c749da4410feda7c6b4b3cc67f4b4f06/src/agent.rs#L50-L83), [src/tools.rs](https://github.com/Phytonking/thread/blob/b5516679c749da4410feda7c6b4b3cc67f4b4f06/src/tools.rs#L496-L550), [src/runtime.rs](https://github.com/Phytonking/thread/blob/b5516679c749da4410feda7c6b4b3cc67f4b4f06/src/runtime.rs#L781-L839), [src/runtime.rs](https://github.com/Phytonking/thread/blob/b5516679c749da4410feda7c6b4b3cc67f4b4f06/src/runtime.rs#L629-L650)
- Basis: Static inspection of pinned first-party source.
- Confidence: medium
- Caveats: Isolation is a supported choice for agents operating in Git workspaces. It does not resolve later conflicts between independently authored branches.

## S3 — Inside-and-now control

- State: A(P)
- Function: Change live coding commitments across the current thread roster.
- Disturbance / variety regulated: Workers may be idle, blocked, redundant or allocated an unsuitable model.
- Decisive decision or feedback right: Choose to start, redirect, remove or reallocate a live worker.
- Decision owner: Main's model in the default agent path. The live REPL operator owns direct removal and redirection in the attended path.
- Supporting / enforcement mechanisms: Roster and worker status, reports, targeted mailbox, model configuration and stoppable workers.
- Closure path: A model stop or direct user removal stops the targeted worker. A follow-up message wakes or steers it, and the selected model applies to later turns.
- Why this is / is not agent-owned: Main and the operator own different reachable intervention paths. The supervisor executes the selected intervention.
- Boundary reachability: The standard binary ships both main's management tools and the roster-aware attended REPL.
- Whole-system current view: Main receives all live workers and their status, mandates and completed reports. The operator examines the same roster via the full terminal list and focused views.
- Current-control decision scope: Select workers, change assignments, reclaim a live slot or change the worker's model.
- Evidence: [src/agent.rs](https://github.com/Phytonking/thread/blob/b5516679c749da4410feda7c6b4b3cc67f4b4f06/src/agent.rs#L275-L301), [src/tools.rs](https://github.com/Phytonking/thread/blob/b5516679c749da4410feda7c6b4b3cc67f4b4f06/src/tools.rs#L554-L617), [src/runtime.rs](https://github.com/Phytonking/thread/blob/b5516679c749da4410feda7c6b4b3cc67f4b4f06/src/runtime.rs#L381-L397), [src/main.rs](https://github.com/Phytonking/thread/blob/b5516679c749da4410feda7c6b4b3cc67f4b4f06/src/main.rs#L550-L582), [src/main.rs](https://github.com/Phytonking/thread/blob/b5516679c749da4410feda7c6b4b3cc67f4b4f06/src/main.rs#L611-L629), [src/main.rs](https://github.com/Phytonking/thread/blob/b5516679c749da4410feda7c6b4b3cc67f4b4f06/src/main.rs#L1061-L1090)
- Basis: Static inspection of pinned first-party source.
- Confidence: medium
- Caveats: A routine approval for one tool is outside the parent S3 witness.

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (`A`) | Main model | Live roster or a returned report | Main selects stop, reassignment or another worker and the supervisor applies it | `src/agent.rs` and `src/tools.rs` |
| Parent (`P`) | Attended REPL operator | Cross-worker roster shows an in-progress commitment that should end or change | Direct removal, focused steering or model reallocation changes the target's operation | `src/main.rs` and `src/runtime.rs` |

## S3* — Complementary audit

- State: —
- Function: Complementary challenge of a worker claim was sought.
- Disturbance / variety regulated: A handoff can overstate the status of a change or a verification result.
- Decisive decision or feedback right: No first-party complementary findings-to-control loop was established for a current worker claim.
- Decision owner: Main receives reports and can commission ordinary coding tasks.
- Supporting / enforcement mechanisms: Read-thread state, recent assistant output, Git worktrees, operator inspection and offline transcript replay.
- Closure path: Progress reading returns worker-authored output. Replay writes learning evidence for another run.
- Why this is / is not agent-owned: A dedicated reviewer can be composed, with its mandate and corrective return chosen ad hoc.
- Evidence: [src/tools.rs](https://github.com/Phytonking/thread/blob/b5516679c749da4410feda7c6b4b3cc67f4b4f06/src/tools.rs#L554-L592), [src/threads.rs](https://github.com/Phytonking/thread/blob/b5516679c749da4410feda7c6b4b3cc67f4b4f06/src/threads.rs#L370-L392), [src/runtime.rs](https://github.com/Phytonking/thread/blob/b5516679c749da4410feda7c6b4b3cc67f4b4f06/src/runtime.rs#L629-L653), [src/consolidate.rs](https://github.com/Phytonking/thread/blob/b5516679c749da4410feda7c6b4b3cc67f4b4f06/src/consolidate.rs#L346-L364)
- Basis: Static inspection of pinned first-party source.
- Confidence: medium
- Caveats: Ordinary tests and review remain available to operators and agents.

### Absence scope

- Surfaces inspected: Background handoff, read_thread, persistent events, terminal trace views and consolidation.
- Plausible first-party paths checked: A supplied intervention that samples a current operational claim through independent source evidence and returns it to main's control.
- Why no material first-party path remains: The supplied read tool exposes the report channel, and transcript replay serves consolidation. Generic worktree access and agent spawning leave the audit loop unspecified.

## S4 — Outside-and-then intelligence

- State: A
- Function: Adapt reusable coding procedure and environmental beliefs for future work.
- Disturbance / variety regulated: Repository or user conditions differ from those assumed in earlier tasks, and repeated runs reveal reusable success patterns.
- Decisive decision or feedback right: Infer changed environment facts or select the procedure to encode for similar future tasks.
- Decision owner: The configured consolidation model.
- Supporting / enforcement mechanisms: Recorded user interactions and tool outcomes, surprise and baseline scoring, skill persistence and relevance retrieval.
- Closure path: Consolidation saves inferred facts and generalized steps. A later task receives the matching capability procedure as a versioned skill in its model prompt.
- Why this is / is not agent-owned: Thresholds decide when to invoke the model. The model supplies the new procedure and the conditions for applying it.
- Boundary reachability: Standard handoff calls consolidation and standard fresh turns consume recalled skills.
- External distinction: User corrections and actual outcomes of tools working against the repository feed the run records.
- Future / prospective distinction: Successful traces across tasks of one kind support a reusable procedure for the next instance.
- Adaptation option generated: The model proposes steps and conditions for a new persistent skill.
- Path back into current capability / S3: Saved, scoped skill material is injected into a later main or worker turn and can guide subsequent tool and planning choices.
- Evidence: [src/runtime.rs](https://github.com/Phytonking/thread/blob/b5516679c749da4410feda7c6b4b3cc67f4b4f06/src/runtime.rs#L629-L669), [src/consolidate.rs](https://github.com/Phytonking/thread/blob/b5516679c749da4410feda7c6b4b3cc67f4b4f06/src/consolidate.rs#L151-L205), [src/consolidate.rs](https://github.com/Phytonking/thread/blob/b5516679c749da4410feda7c6b4b3cc67f4b4f06/src/consolidate.rs#L285-L305), [src/consolidate.rs](https://github.com/Phytonking/thread/blob/b5516679c749da4410feda7c6b4b3cc67f4b4f06/src/consolidate.rs#L346-L419), [src/consolidate.rs](https://github.com/Phytonking/thread/blob/b5516679c749da4410feda7c6b4b3cc67f4b4f06/src/consolidate.rs#L476-L514), [src/agent.rs](https://github.com/Phytonking/thread/blob/b5516679c749da4410feda7c6b4b3cc67f4b4f06/src/agent.rs#L314-L341), [src/agent.rs](https://github.com/Phytonking/thread/blob/b5516679c749da4410feda7c6b4b3cc67f4b4f06/src/agent.rs#L359-L384)
- Basis: Static inspection of pinned first-party source.
- Confidence: medium
- Caveats: The procedure is a tentative or promoted prompt capability. Adoption in each task remains model-dependent.

## S5 — Policy and identity

- State: —
- Function: Resolve organizational identity or ultimate-policy issues.
- Disturbance / variety regulated: A requested operation may exceed a configured workspace or permission boundary.
- Decisive decision or feedback right: No identity issue admission, authority judgment and returned policy decision was found.
- Decision owner: The user sets provider and action permissions. The harness enforces the selected workspace scope.
- Supporting / enforcement mechanisms: Provider choice, workdir zone and single-action approvals.
- Closure path: Standard tools apply the configured operating boundaries, including decisions for named action classes.
- Why this is / is not agent-owned: The supplied switches configure operational limits and do not supply ultimate-policy adjudication.
- Evidence: [src/main.rs](https://github.com/Phytonking/thread/blob/b5516679c749da4410feda7c6b4b3cc67f4b4f06/src/main.rs#L199-L259), [src/main.rs](https://github.com/Phytonking/thread/blob/b5516679c749da4410feda7c6b4b3cc67f4b4f06/src/main.rs#L526-L546), [src/main.rs](https://github.com/Phytonking/thread/blob/b5516679c749da4410feda7c6b4b3cc67f4b4f06/src/main.rs#L824-L869), [src/zone.rs](https://github.com/Phytonking/thread/blob/b5516679c749da4410feda7c6b4b3cc67f4b4f06/src/zone.rs#L25-L80), [docs/commands.md](https://github.com/Phytonking/thread/blob/b5516679c749da4410feda7c6b4b3cc67f4b4f06/docs/commands.md#L40-L52)
- Basis: Static inspection of pinned first-party source.
- Confidence: medium
- Caveats: Maintainers and provider organizational authorities are outside a repository-local runtime.

### Absence scope

- Surfaces inspected: REPL authority, provider and workspace configuration, action approvals and enforced zone.
- Plausible first-party paths checked: A policy dispute or identity escalation adjudicated by main or by a legitimate parent and returned as a governing resolution.
- Why no material first-party path remains: The available functions configure or enforce workspace and tool rights, and the project has no higher-order runtime adjudication channel for identity.

## Recursion

One coordinator and multiple worker operations share a repository boundary. A model backend or Git worktree does not form another autonomous organizational recursion.

## Variety and escalation

Inbox messages, approval prompts, workspace boundaries and model selection constrain operational variety. Worker handoffs surface critical local decisions to main. Direct terminal intervention is available to the operator.

## Evidence gaps

Static review. No models, provider commands, live worker race, approval or consolidation loop were executed. No outcome improvement from recalled procedures was measured.
