---
harness_id: claude-squad
project_name: Claude Squad
repository: https://github.com/smtg-ai/claude-squad
review_ref: ce1ffb4392b01f38e2c4599c7c84d2a93973b138
reviewed_at: 2026-09-19
generated_profile_version: 0.2.3
generated_assessment_procedure_version: 0.3.5
profile_version: 0.2.3
assessment_procedure_version: 0.3.5
assessment_changed_at: 2026-09-19
status: included
autonomy_s1: A
autonomy_s2: C
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Claude Squad

## Review boundary

- System in focus: the shipped Claude Squad terminal harness at pinned revision `ce1ffb4392b01f38e2c4599c7c84d2a93973b138`, including first-party TUI/session lifecycle, per-session tmux hosting, git-worktree/branch isolation, prompt injection, status/diff monitoring, persistence, pause/resume/kill/checkout/push controls, and the supported managed coding-agent processes running inside those sessions.
- Purpose and identity: run several autonomous terminal coding agents against one repository in parallel while keeping their workspaces isolated and giving an operator one durable terminal surface for creating, prompting, monitoring, reviewing and integrating their work.
- Relevant environment: user-supplied coding tasks/prompts; the target git repository and branches; filesystem/code state; external Claude Code/Codex/Gemini/Aider or custom terminal-agent behavior; tmux/process state; generated diffs; operator lifecycle and integration decisions.
- Standard-distribution boundary: the installable `cs` binary and its supported local operating mode, in which Claude Squad deliberately launches configured autonomous coding-agent programs inside first-party-managed tmux sessions and git worktrees. The internal reasoning/model/tool implementation of Claude Code, Codex, Gemini, Aider and arbitrary custom programs is external substrate and is not borrowed to establish higher VSM functions; those supported managed processes are nevertheless operational agent actors inside the declared assembled harness boundary.
- Credited operating / distribution surfaces: `app/` TUI and instance list; `session/instance.go`; `session/tmux/`; `session/git/`; persisted instance/config state; prompt/status/diff plumbing; documented standard profiles and background-agent operation.
- Adjacent first-party surfaces excluded from ownership: repository CI/build/lint/release/CLA workflows, tests, website/pages assets, installer/release mechanics, maintainer/contributor governance and documentation-only examples. No external coding agent's private planner, verifier, memory, self-improvement or policy subsystem is imported as Claude Squad-owned metasystem evidence.
- First-party operating / deployment modes considered: one or more simultaneous Claude Code/Codex/Gemini/Aider/custom agent sessions; new-session-with-prompt; background execution; optional `--autoyes`; operator review/diff/push/checkout/pause/resume/kill; restored persisted sessions after restarting Claude Squad.
- Recursion level: one Claude Squad-managed local repository workspace as the system-in-focus. Each supported autonomous coding-agent session performing a distinct task in its own worktree is an S1 operational unit. The TUI/session/worktree manager is assessed as harness/metasystem machinery around those S1 units.
- Reviewed revision: `ce1ffb4392b01f38e2c4599c7c84d2a93973b138`.
- Stable GitHub repository id: `945605057`.
- Observation date: 2026-09-19.
- Generated Profile version: `0.2.3`.
- Generated Methodology version: `0.3.5`.
- Current Profile version: `0.2.3`.
- Current Methodology version: `0.3.5`.

## Repository architecture

Claude Squad is a Go TUI around external autonomous terminal coding agents. A new `Instance` receives a configured program such as `claude`, `codex`, `gemini`, or `aider`; Claude Squad creates a dedicated git branch/worktree and starts the program in a dedicated tmux session rooted at that worktree. The TUI can send an initial or later prompt, persist and restore sessions, capture terminal output, derive Running/Ready state from pane activity, show per-instance diffs, and optionally auto-press confirmation prompts in `--autoyes` mode.

The operational intelligence remains in the hosted coding-agent process. Claude Squad does not implement the model/tool reasoning loop of Claude Code or Codex. At the declared assembled-harness boundary, however, those supported autonomous processes are not adjacent repository dogfood: launching and managing them is the product's primary runtime purpose, and they execute the user's coding transformations inside Claude Squad-created environments. That establishes S1 without importing their private internals as evidence for S2-S5.

The main cross-S1 mechanism is workspace isolation. The project explicitly states that each task receives its own isolated git workspace "so no conflicts". `NewGitWorktree` creates a branch and unique worktree path per session before the agent program is launched there. This is a concrete structural interference witness: parallel coding agents aimed at one repository could collide through shared working-tree/index/file state; Claude Squad separates their write environments so subsequent agent actions do not contend on that mutable workspace. The isolation policy is deterministic and operator/config selected; Claude Squad does not ship an autonomous coordination actor that negotiates or revises that response, so the S2 path is constructor-level rather than agent-owned.

The TUI also exposes current session status, ordering, preview/diff, pause/resume/kill, checkout and push. Those are useful lifecycle and integration controls, but the reviewed system does not turn them into an autonomous whole-system S3 loop. Human diff review and confirmation before push likewise do not become S3* or S5 merely because the operator can make a final local decision.

## Operational model

A user creates one or more sessions and gives each a coding prompt. Claude Squad creates an isolated branch/worktree, launches the chosen autonomous coding CLI in tmux and sends the prompt. The hosted agent then performs its own coding/tool loop against that worktree. Claude Squad monitors pane changes and git diffs, persists instance metadata and lets the user detach while work continues. Multiple sessions can therefore produce independent code changes concurrently.

For coordination, the harness does not route messages or negotiate plans among agents. Instead it attenuates a concrete shared-repository collision class before work starts: every session gets a separate git worktree/branch and the agent process is launched with that path as its working directory. Integration is later operator-owned through review, checkout/pause and push controls.

## S1 — Operations

- State: A
- Function: autonomously perform coding tasks that transform the target repository/environment inside a Claude Squad-managed session.
- Disturbance / variety regulated: heterogeneous coding prompts, repository/file state, compilation/test/tool feedback and other task-local uncertainty encountered by the hosted autonomous coding agent.
- Decisive decision or feedback right: choose the coding/tool actions required to satisfy the assigned prompt, observe resulting repository/tool state, and continue or finish the task.
- Decision owner: the supported autonomous terminal coding-agent process (for example Claude Code, Codex, Gemini or Aider) running as the operational actor inside the Claude Squad-managed session.
- Supporting / enforcement mechanisms: Claude Squad tmux lifecycle, prompt injection, per-session git branch/worktree, persisted session metadata, terminal/status capture, diff monitoring and optional automatic confirmation keystrokes.
- Closure path: user assigns prompt → Claude Squad launches/sends it to the managed coding-agent process in its worktree → agent autonomously acts on code/tools and observes results → agent continues its local loop and produces repository changes/output visible through the session/diff surfaces.
- Boundary reachability: hosting these agent programs is Claude Squad's documented standard product mode, not an adjacent example or developer workflow. The TUI directly starts the configured program in the first-party-created worktree and sends prompts to it, so the autonomous operational actor is reachable in the supported assembled distribution.
- Why this is / is not agent-owned: removing the hosted coding-agent process while leaving tmux, worktree, persistence and TUI machinery leaves no actor that interprets the coding prompt and chooses repository-changing actions. Claude Squad supplies the harness around that autonomous S1 rather than owning the model's local decisions itself.
- Evidence: [`README.md`](https://github.com/smtg-ai/claude-squad/blob/ce1ffb4392b01f38e2c4599c7c84d2a93973b138/README.md), [`session/instance.go`](https://github.com/smtg-ai/claude-squad/blob/ce1ffb4392b01f38e2c4599c7c84d2a93973b138/session/instance.go), [`session/tmux/tmux.go`](https://github.com/smtg-ai/claude-squad/blob/ce1ffb4392b01f38e2c4599c7c84d2a93973b138/session/tmux/tmux.go), [`app/app.go`](https://github.com/smtg-ai/claude-squad/blob/ce1ffb4392b01f38e2c4599c7c84d2a93973b138/app/app.go).
- Basis: explicit
- Confidence: high
- Caveats: Claude Squad does not own the external agent executable/model internals; only the operational actor's role in the intentionally assembled supported runtime is credited. No higher function is inferred from undocumented capabilities of those external agents.

## S2 — Coordination

- State: C
- Function: prevent destructive workspace/git-state interference among concurrent coding-agent S1 sessions operating on tasks in the same repository.
- Disturbance / variety regulated: simultaneous agents writing files/index/worktree state in one shared checkout could overwrite, mix or otherwise conflict with one another's task-local repository changes.
- Decisive decision or feedback right: assign each concurrent task/session an isolated branch/worktree before its agent starts, thereby selecting a non-shared mutable workspace for subsequent S1 actions. The first-party path is S2-specific, but an autonomous actor that decides or revises this coordination response is not supplied.
- Decision owner: constructor-level. Claude Squad deterministically enforces per-session isolation under operator-created sessions; a deployment would need to compose an autonomous coordination actor/authority if it wanted agent-owned discretion over when/how to isolate, reconcile or revise the coordination response.
- Supporting / enforcement mechanisms: unique worktree directory generation, per-session branch names, tmux startup with the worktree as `-c` working directory, branch preservation across pause/resume and later operator integration controls.
- Closure path: concurrent task/session creation → Claude Squad creates distinct branches/worktrees → each coding-agent S1 is launched inside its assigned worktree → its later file/git writes remain separated from other active sessions' mutable workspaces.
- Boundary reachability: the isolation relation is mandatory first-party startup behavior in the normal multi-session product mode and is explicitly documented as the reason parallel tasks avoid conflicts; it does not depend on tests, CI or external agent internals.
- Why this is / is not agent-owned: the S2 function and attenuation path are supplied, but the hosted agents do not choose or negotiate the coordination response. Deterministic isolation enforces a preselected policy; therefore it does not meet `A`, while the dedicated conflict-prevention path is more specific than generic routing/shared-state extensibility and meets the constructor threshold.
- Distinct S1 units: at least two simultaneously managed autonomous coding-agent sessions, each assigned a separate coding task and worktree.
- Inter-S1 disturbance: concurrent edits/git operations against one repository checkout would contend on shared mutable workspace/index/file state; the README states each task uses an isolated git workspace "so no conflicts".
- Attenuating coordination relation: Claude Squad creates a unique branch/worktree for every session and starts that agent's tmux program inside that isolated worktree.
- Feedback into subsequent S1 behaviour: the selected isolation is embodied in each agent's working directory; all subsequent task-local file/git actions occur against that separated state rather than the other S1s' workspaces.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the mechanism is explicitly tied to attenuating a named cross-worker collision mode caused by parallel repository modification. It does not receive credit merely because Claude Squad launches multiple processes or has a session list.
- Evidence: [`README.md`](https://github.com/smtg-ai/claude-squad/blob/ce1ffb4392b01f38e2c4599c7c84d2a93973b138/README.md), [`session/git/worktree.go`](https://github.com/smtg-ai/claude-squad/blob/ce1ffb4392b01f38e2c4599c7c84d2a93973b138/session/git/worktree.go), [`session/instance.go`](https://github.com/smtg-ai/claude-squad/blob/ce1ffb4392b01f38e2c4599c7c84d2a93973b138/session/instance.go), [`session/tmux/tmux.go`](https://github.com/smtg-ai/claude-squad/blob/ce1ffb4392b01f38e2c4599c7c84d2a93973b138/session/tmux/tmux.go).
- Basis: explicit
- Confidence: high
- Caveats: isolation prevents one important collision class but does not constitute rich mutual adjustment or automated branch reconciliation. Human integration decisions are outside S2 parent notation and are not used to upgrade the constructor state.

## S3 — Inside-and-now control

- State: —
- Function: no material first-party whole-system current-control loop was established beyond session lifecycle management and fixed capacity/configuration constraints.
- Disturbance / variety regulated: candidate paths included the global list of sessions, Running/Ready/Loading/Paused status, a fixed 10-instance limit, instance ordering, diff/preview panes, create/kill/pause/resume and push/checkout actions.
- Decisive decision or feedback right: no agent or first-party S3-specific constructor was found that receives a whole-system current operational picture and decides shared resource allocation, commitment reprioritization, synergy or intervention on behalf of the multi-session whole.
- Decision owner: none established for S3 at the assessed recursion.
- Supporting / enforcement mechanisms: TUI list/status display, `GlobalInstanceLimit`, per-instance metadata/diff refresh, lifecycle commands, confirmations and tmux/worktree state.
- Closure path: operator commands can change an individual session's lifecycle or integrate one branch, but no S3-specific whole-system regulation loop was found.
- Why this is / is not agent-owned: showing several sessions and allowing a human to pause/kill/reorder one is management UI, not autonomous inside-and-now control. The hosted coding agents do not receive the whole-session view or authority to regulate the other sessions through Claude Squad.
- Evidence: [`app/app.go`](https://github.com/smtg-ai/claude-squad/blob/ce1ffb4392b01f38e2c4599c7c84d2a93973b138/app/app.go), [`session/instance.go`](https://github.com/smtg-ai/claude-squad/blob/ce1ffb4392b01f38e2c4599c7c84d2a93973b138/session/instance.go).
- Basis: structural
- Confidence: high
- Caveats: an operator may of course coordinate priorities manually outside the harness; ordinary human session management does not qualify as published S3 parent mode without a reconstructable whole-system S3 loop.

### Absence scope

- Surfaces inspected: TUI home/session list, status updater, global instance limit, ordering controls, pause/resume/kill, prompt injection, diff/preview and push/checkout actions, persisted instance state.
- Plausible first-party paths checked: multi-session status as a possible whole-system view; fixed concurrency/capacity; operator reorder; kill/pause/resume; branch checkout/push; hosted agent access to other sessions.
- Why no material first-party path remains: the reviewed paths are per-session lifecycle/integration controls or static enforcement. No autonomous/controller actor owns a current resource/commitment decision across the whole set of S1s, and no S3-specific constructor exposes that decision right for composition.

## S3* — Complementary audit

- State: —
- Function: no materially independent first-party complementary audit loop with findings returned into subsequent operational control was established.
- Disturbance / variety regulated: candidate evidence included the diff tab, terminal preview/history and the documented ability to review changes before applying/pushing them.
- Decisive decision or feedback right: the human operator can inspect diffs and decide whether to push/checkout, but Claude Squad supplies no autonomous or constructor audit actor that independently challenges an S1 claim/result and returns a corrective finding into that S1's execution.
- Decision owner: none established in the Methodology's S3* publication states.
- Supporting / enforcement mechanisms: git diff computation/display, terminal capture, push confirmation and checkout/pause workflow.
- Closure path: human inspection may lead to manual reprompting or refusal to integrate, but no first-party complementary audit judgment→corrective-return loop is encoded as an autonomous/constructor S3* path.
- Why this is / is not agent-owned: review UI gives a human alternative access to artifacts, but Methodology 0.3.x does not publish parent-mode S3* and ordinary human review cannot be relabelled autonomous audit.
- Evidence: [`README.md`](https://github.com/smtg-ai/claude-squad/blob/ce1ffb4392b01f38e2c4599c7c84d2a93973b138/README.md), [`app/app.go`](https://github.com/smtg-ai/claude-squad/blob/ce1ffb4392b01f38e2c4599c7c84d2a93973b138/app/app.go), [`session/instance.go`](https://github.com/smtg-ai/claude-squad/blob/ce1ffb4392b01f38e2c4599c7c84d2a93973b138/session/instance.go).
- Basis: structural
- Confidence: high
- Caveats: external coding agents may implement their own review/verifier features internally, but those are not Claude Squad-owned or wired as a first-party complementary audit relation.

### Absence scope

- Surfaces inspected: diff computation/display, preview/terminal capture, push confirmation, checkout/pause, reprompt/attach controls and README review workflow.
- Plausible first-party paths checked: human diff review, status/terminal observation, confirmation before push/apply, external agent self-review and manual reprompting.
- Why no material first-party path remains: all first-party review surfaces are observational/operator-driven and lack a dedicated independent autonomous audit judgment with corrective return; external agent-private review cannot be borrowed across the boundary.

## S4 — Outside-and-then intelligence

- State: —
- Function: no first-party externally/prospectively oriented adaptation loop was established for changing Claude Squad's future operational capability.
- Disturbance / variety regulated: candidate paths included multiple configurable agent profiles/programs, operator reprompting, persisted state, release/update mechanics and the ability to resume sessions.
- Decisive decision or feedback right: no first-party path senses external/future distinctions, develops an adaptation option and returns it to alter the harness's capability for subsequent work.
- Decision owner: none established for S4.
- Supporting / enforcement mechanisms: static profile configuration, program command selection, persistence and lifecycle controls.
- Closure path: changing a profile/program selects an already available external agent command; it does not constitute prospective capability development by the harness.
- Why this is / is not agent-owned: hosted coding agents adapt within their assigned coding tasks, but no Claude Squad metasystem actor studies the future/external environment and changes the harness's repertoire.
- Evidence: [`README.md`](https://github.com/smtg-ai/claude-squad/blob/ce1ffb4392b01f38e2c4599c7c84d2a93973b138/README.md), [`config/config.go`](https://github.com/smtg-ai/claude-squad/blob/ce1ffb4392b01f38e2c4599c7c84d2a93973b138/config/config.go), [`app/app.go`](https://github.com/smtg-ai/claude-squad/blob/ce1ffb4392b01f38e2c4599c7c84d2a93973b138/app/app.go).
- Basis: structural
- Confidence: high
- Caveats: arbitrary external programs can be configured, but general extensibility/selection is not an S4-specific adaptation constructor.

### Absence scope

- Surfaces inspected: profiles/default program configuration, session persistence/recovery, prompt/lifecycle paths, repository workflows/docs and external-program integration.
- Plausible first-party paths checked: selecting a different coding agent, updating profiles, learning from completed sessions/diffs, automatic harness reconfiguration, repository release/update machinery.
- Why no material first-party path remains: reviewed product paths select or operate existing capabilities; none closes external/future sensing → adaptation-option generation → return into current capability.

## S5 — Policy and identity

- State: —
- Function: no runtime identity/ultimate-policy decision path was established at the multi-session system recursion.
- Disturbance / variety regulated: candidate paths included configuration profiles, `--autoyes`, trust-prompt handling, kill/push confirmations, branch selection and operator control of sessions.
- Decisive decision or feedback right: no identity/ultimate-policy issue is escalated to an ultimate authority and returned as durable policy governing later operation.
- Decision owner: none established for S5.
- Supporting / enforcement mechanisms: config file, profile/program choice, automatic confirmation behavior, TUI confirmation overlays, tmux trust-prompt handling and ordinary operator commands.
- Closure path: confirmations affect individual operational actions; they do not close system identity/ultimate-policy tension at the declared recursion.
- Why this is / is not agent-owned: the human has final say over ordinary push/kill/session actions, but final say on a task action is not S5. External coding agents' system prompts/policies are outside Claude Squad ownership.
- Evidence: [`README.md`](https://github.com/smtg-ai/claude-squad/blob/ce1ffb4392b01f38e2c4599c7c84d2a93973b138/README.md), [`app/app.go`](https://github.com/smtg-ai/claude-squad/blob/ce1ffb4392b01f38e2c4599c7c84d2a93973b138/app/app.go), [`session/tmux/tmux.go`](https://github.com/smtg-ai/claude-squad/blob/ce1ffb4392b01f38e2c4599c7c84d2a93973b138/session/tmux/tmux.go).
- Basis: structural
- Confidence: high
- Caveats: operator ownership is intentionally strong in this tool, but the observed decisions are operational/integration controls rather than identity-level governance.

### Absence scope

- Surfaces inspected: configuration/profile loading, `--autoyes`, trust prompts, human confirmation overlays, push/kill/checkout/session lifecycle, README and adjacent repository governance.
- Plausible first-party paths checked: operator final approval, static program/profile policy, trust/security prompts, maintainer/project policy and external agent system instructions.
- Why no material first-party path remains: no product-runtime path handles an identity/ultimate-policy issue with legitimate ultimate authority and returned policy closure; ordinary confirmations and external-agent policy remain outside that function/boundary.

## Recursion

Each managed coding-agent session can itself contain a sophisticated viable system implemented by the external agent product, but Claude Squad does not receive credit for those private internal metasystems. At the assessed recursion the sessions are S1 operational units inside a local multi-task repository harness. Worktree isolation supplies one cross-S1 S2 construction path; higher functions require evidence at this wider recursion and are not inferred from nested agent sophistication.

## Variety and escalation

Claude Squad attenuates parallel-work variety primarily by separating mutable repository state into worktrees and by representing each session with a small lifecycle/status vocabulary. It amplifies operational capacity by allowing up to ten background coding sessions and preserving their branches/state across detachment or restart. Integration decisions escalate to the human through diff/preview and push/checkout controls, but those operator actions retain their actual operational meaning rather than being promoted to S3*/S5.

## Evidence gaps

- The S2 constructor claim is deliberately narrow: it covers workspace/git-state collision attenuation, not general task dependency management, negotiation or merge-conflict resolution.
- No first-party autonomous actor was found that chooses/revises the S2 isolation policy, so `A` is not justified.
- External coding agents can contain their own planners, reviewers, memory and policies; none of those private functions are counted for Claude Squad S3-S5 without a first-party cross-session closure.
