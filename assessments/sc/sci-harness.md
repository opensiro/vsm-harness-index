---
harness_id: sci-harness
project_name: Sci-Harness
repository: https://github.com/Nag681/sci-harness
review_ref: e241a6e930788498d87e7cc3172fe63cf6dd486c
reviewed_at: 2026-10-26
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: —
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Sci-Harness

## Review boundary

- System in focus: the installed `sci` Agent Skill and Python `.sci/sci` project referee, with optional agent-host hook integration at frozen SHA; not the host coding agent's full harness or a project developed with it.
- Purpose and identity: preserve long-running scientific coding workflow state, establish test/golden baselines, protect acceptance tests, refuse out-of-scope or unverified changes, track failed attempts and guide external agents toward an evidence-based next step.
- Relevant environment: user Git repositories and tests, scientific/numerical code, shell/Python tools, and separately installed host agents (Claude Code, Codex CLI, Gemini CLI, OpenCode, pi and others).
- Standard-distribution boundary: `SKILL.md`, `scripts/sci.py`, optional `scripts/sci_hook.py`, installers and their generated `.sci/` state. The agent that actually observes code, reasons, chooses edits and runs these commands is explicitly a separate installed product.
- Credited operating / distribution surfaces: Python state and test-verification CLI, skill instructions, install/copy/symlink paths, hook guards when selected by `--hooks`, local recovery/commit and test-lock logic.
- Adjacent first-party surfaces excluded from ownership: development unit/integration tests, README's worked-example transcripts, external host agent/model/tool-selection loops, actual project test suites and human review judgments. These may demonstrate the referee's mechanism without making the external agent's cognition a first-party Sci-Harness controller.
- First-party operating / deployment modes considered: skill-only instruction mode, optional hooks in agent host, persistent `.sci/` task/status/check/verify/hypothesis/restore workflow, commit-on-done and human review flags.
- Recursion level: one installed `sci` workflow for a user repository, not the agent host or the Sci-Harness OSS development organization.
- Reviewed revision: `e241a6e930788498d87e7cc3172fe63cf6dd486c`.
- Observation date: 2026-10-26.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

The [README](https://github.com/Nag681/sci-harness/blob/e241a6e930788498d87e7cc3172fe63cf6dd486c/README.md) and first-party [`SKILL.md`](https://github.com/Nag681/sci-harness/blob/e241a6e930788498d87e7cc3172fe63cf6dd486c/SKILL.md) direct the user to install the skill into an existing coding agent and ask *that* agent to work. The agent reads `NEXT:` guidance, writes and tests code, asks domain questions, proposes hypotheses and issues `.sci/sci` commands. The repository does not package an LLM call loop, model adapter, autonomous editing agent or a first-party runtime that chooses next repository actions from tool results.

[`sci.py`](https://github.com/Nag681/sci-harness/blob/e241a6e930788498d87e7cc3172fe63cf6dd486c/scripts/sci.py) is substantial deterministic enforcement: durable tasks/notes/hypotheses, state-file locking, scoped file checks, immutable test hashes, golden comparisons, baseline/regression runs, strike/STOP handling, safe attempt snapshots, verification and commits. It launches *operator/agent-selected test commands* through subprocess, but those test subprocesses do not constitute autonomous AI operating cells. Optional [`sci_hook.py`](https://github.com/Nag681/sci-harness/blob/e241a6e930788498d87e7cc3172fe63cf6dd486c/scripts/sci_hook.py) injects session reorientation and detects selected destructive shell commands. It is an external host hook callback, not a new model actor.

The dependency-free [installer](https://github.com/Nag681/sci-harness/blob/e241a6e930788498d87e7cc3172fe63cf6dd486c/install.py) copies or links the skill to external agent hosts, optionally registering hooks. That explicitly reconstructs the dependency boundary: without the separately installed host agent, `.sci/sci` can retain and validate state but cannot itself carry out the creative coding task. Reproduction of the deterministic mechanisms through tests is not a model-quality result.

## Operational model and admission decision

Human asks an external coding agent for a scientific coding task → the host agent uses the supplied skill plan and `.sci/sci` commands → Sci-Harness records/refuses/verifies actions, returns `NEXT:` and test evidence → the **external** agent interprets that evidence and chooses the next code change, hypothesis or escalation. Sci-Harness supplies strong constraints and durable feedback, but no first-party autonomous operational actor closes the task-specific model/tool/action loop at this declared repository boundary.

**Proposed canonical disposition: `excluded-no-agentic-vsm`**, vector `— — — — — —`. This conclusion is about first-party operational ownership, not the utility or correctness of the skill, the agentic nature of a *composed* host+skill deployment, or whether its deterministic verification can support a separate organization.

## S1 — Operations

- State: —
- Function: no first-party autonomous scientific-coding operational decision/action loop is shipped.
- Disturbance / variety regulated: unknown code changes, failing tests, hypotheses and domain ambiguities are resolved by the separately installed agent; the Python referee records and gates steps.
- Decisive decision or feedback right: choose the next substantive code investigation, edit, experiment or hypothesis from observations.
- Decision owner: external host agent (and human for unclear domain goals); `sci.py` enforces selected commands and state transitions.
- Supporting / enforcement mechanisms: `SKILL.md` prompts, `resume/NEXT`, test lock and baseline, strike/STOP, safe restore and verification.
- Closure path: external agent chooses command → Sci-Harness returns status and refusal/evidence → external agent decides the next action; the cognitive/task loop closes outside the first-party package.
- Why this is / is not agent-owned: the host is genuinely agentic, but it is not a first-party actor created, hosted or controlled as an autonomous execution loop by this repository; removing it leaves a deterministic CLI, not a coding agent.
- Evidence: [SKILL.md](https://github.com/Nag681/sci-harness/blob/e241a6e930788498d87e7cc3172fe63cf6dd486c/SKILL.md), [install.py](https://github.com/Nag681/sci-harness/blob/e241a6e930788498d87e7cc3172fe63cf6dd486c/install.py), [sci.py](https://github.com/Nag681/sci-harness/blob/e241a6e930788498d87e7cc3172fe63cf6dd486c/scripts/sci.py).
- Basis: explicit and structural bounded negative.
- Confidence: high.
- Caveats: a separately declared composite installed-agent boundary could have S1=A; it is not silently credited as Sci-Harness-owned autonomy here.

### Absence scope

- Surfaces inspected: README/installers, SKILL task loop, Python command dispatcher and subprocess usage, hook integration and test fixtures.
- Plausible first-party paths checked: `sci resume/NEXT` as an autonomous scheduler, `run/check/verify` as execution agents, `--hooks` as a model loop, and external host support as shipped cognition.
- Why no material first-party path remains: all dynamic coding/tool/hypothesis choices require an independently installed host agent; the referee only constrains and reports those choices.

## S2 — Coordination

- State: —
- Function: no coordination among two distinct first-party autonomous S1 units is established.
- Disturbance / variety regulated: task scopes, dependencies and state-file concurrency prevent operator/host workflow errors, not observed interference among two Sci-Harness-owned S1s.
- Decisive decision or feedback right: revise a joint agent coordination response to an inter-S1 disturbance.
- Decision owner: external host agent/operator chooses task sequence; file/state locks are deterministic.
- Supporting / enforcement mechanisms: `state_lock`, task dependencies/readiness, one-active-task rule and file scope checks.
- Closure path: an invalid command is refused with `NEXT:` guidance; no multi-S1 organizational feedback loop arises.
- Why this is / is not agent-owned: serialization is concrete engineering but not a positive S2 witness without two owned operating cells and their interaction.
- Evidence: [sci.py](https://github.com/Nag681/sci-harness/blob/e241a6e930788498d87e7cc3172fe63cf6dd486c/scripts/sci.py), [SKILL.md](https://github.com/Nag681/sci-harness/blob/e241a6e930788498d87e7cc3172fe63cf6dd486c/SKILL.md).
- Basis: structural bounded negative.
- Confidence: high.
- Caveats: project task dependencies are not S1 units by name alone.

### Absence scope

- Surfaces inspected: task dependency code, state locks, task scope checks, single active task and install modes.
- Plausible first-party paths checked: mutex as conflict arbitration, sequential tasks as multiple S1s and hooks as peer coordination.
- Why no material first-party path remains: these order commands for one external actor rather than attenuate an evidenced interaction between distinct first-party operating units.

## S3 — Inside-and-now control

- State: —
- Function: no closed first-party whole-current control of an autonomous S1 portfolio.
- Disturbance / variety regulated: task status, verification outcome and strike limits inside one host-driven coding workflow.
- Decisive decision or feedback right: choose and revise whole-system operational resources, commitments and interventions.
- Decision owner: external host agent chooses plan and rework; Python guards implement predefined acceptance and STOP conditions.
- Supporting / enforcement mechanisms: persistent task board, output summaries, current-task selection, strike counter and deterministic completion gate.
- Closure path: verifier and strike results direct the external agent to reconsider work; they do not constitute a first-party agent-owned whole-current regulator.
- Why this is / is not agent-owned: a robust bounded task controller is not autonomous S3 discretion; task labels are not independent S1s.
- Evidence: [sci.py](https://github.com/Nag681/sci-harness/blob/e241a6e930788498d87e7cc3172fe63cf6dd486c/scripts/sci.py), [SKILL.md](https://github.com/Nag681/sci-harness/blob/e241a6e930788498d87e7cc3172fe63cf6dd486c/SKILL.md).
- Basis: structural bounded negative.
- Confidence: high.
- Caveats: deterministic control is meaningful S3 support in a wider composed deployment but does not own the decision at this boundary.

### Absence scope

- Surfaces inspected: task start/done, verifier gates, dependency/priority fields, STOP/recovery and status/report.
- Plausible first-party paths checked: task board as whole-system view, failure STOP as S3 intervention, test acceptance as accountability.
- Why no material first-party path remains: current task gates do not decide allocations across first-party autonomous operating units; governing rework choices remain external.

## S3* — Complementary audit

- State: —
- Function: the first-party referee verifies current work with tests/goldens, but no separate complementary independent organizational audit ownership path is established.
- Disturbance / variety regulated: the producing agent may alter tests, loosen tolerances, misstate success or regress earlier work.
- Decisive decision or feedback right: a separately independent audit judgment over raw operational reality with return into whole-system control is not packaged.
- Decision owner: `sci.py` performs deterministic normal acceptance checks and the same external agent supplies/follows test commands, locks and unlock reasons; human reviews flagged exceptions outside an integrated audit mandate.
- Supporting / enforcement mechanisms: test hash locks, baseline/regression checks, golden outputs, tamper detection, refusal and review ledger.
- Closure path: failed verification blocks `done` and returns to the operating agent; no independently positioned audit actor controls a complementary challenge/return channel beyond this mandatory same-task QA.
- Why this is / is not agent-owned: tests are stronger than self-report, but routine integrated test-lock/verify gates are not automatically S3*; optional hooks do not create independent audit judgment.
- Evidence: [sci.py](https://github.com/Nag681/sci-harness/blob/e241a6e930788498d87e7cc3172fe63cf6dd486c/scripts/sci.py), [scientific verification](https://github.com/Nag681/sci-harness/blob/e241a6e930788498d87e7cc3172fe63cf6dd486c/references/scientific-verification.md).
- Basis: structural bounded negative.
- Confidence: medium-high.
- Caveats: direct artifact checks are useful complementary evidence for a separately established parent audit, but this boundary lacks that independent authority/reachability.

### Absence scope

- Surfaces inspected: lock/verify/baseline/golden/restore code, review flags, hook guards, agent instructions and tests.
- Plausible first-party paths checked: referee as independent auditor, locked tests as independent ground truth, operator review requests as audit return.
- Why no material first-party path remains: mandatory same-workflow QA uses criteria/workflow authored and changed by the producing external actor; no distinct sufficiently independent audit governance and corrective return is wired for the assessed installation.

## S4 — Outside-and-then intelligence

- State: —
- Function: no first-party external/prospective environmental adaptation loop is supplied.
- Disturbance / variety regulated: changing task facts, hypotheses and numerical behaviour are current work observations, not prospective capability-market/environment intelligence.
- Decisive decision or feedback right: select future organizational adaptations from developed external options.
- Decision owner: user or outside coding agent revises task approach; Python records evidence and constraints.
- Supporting / enforcement mechanisms: saved notes, hypotheses, goldens, debugging/large-codebase reference guides and resume summaries.
- Closure path: evidence can improve the next current task step, but does not change future system capability through an independently controlled S4–S3 loop.
- Why this is / is not agent-owned: scientific hypotheses after failed attempts are task-level problem solving, not future-facing strategic adaptation.
- Evidence: [SKILL.md](https://github.com/Nag681/sci-harness/blob/e241a6e930788498d87e7cc3172fe63cf6dd486c/SKILL.md), [sci.py](https://github.com/Nag681/sci-harness/blob/e241a6e930788498d87e7cc3172fe63cf6dd486c/scripts/sci.py).
- Basis: structural bounded negative.
- Confidence: high.
- Caveats: future self-improvement under an outside organization is not assessed.

### Absence scope

- Surfaces inspected: hypothesis/notes persistence, scientific guides, goldens, baseline, hooks and project status.
- Plausible first-party paths checked: hypothesis recovery as learning, notebook as capability memory, test-driven changes as adaptation.
- Why no material first-party path remains: all are current project-work controls without external prospecting and returned capability adaptation.

## S5 — Policy and identity

- State: —
- Function: no ultimate identity/policy decision and authoritative return path in this local skill installation.
- Disturbance / variety regulated: unsafe edits, locked tests and dangerous Git actions are constrained by preselected work rules.
- Decisive decision or feedback right: identity-level policy resolution is outside the referee.
- Decision owner: human sets goal and may review unlock reasons; the host agent applies task instructions, Python enforces rule checks.
- Supporting / enforcement mechanisms: SKILL directives, test protection, optional pre-tool hooks, STOP, safe undo and report flags.
- Closure path: rule refusal affects an ordinary command, not an identity-policy issue adjudicated by legitimate parent authority and returned as durable operating policy.
- Why this is / is not agent-owned: static anti-shortcut instructions and human review do not establish ultimate S5 merely because they constrain a model.
- Evidence: [SKILL.md](https://github.com/Nag681/sci-harness/blob/e241a6e930788498d87e7cc3172fe63cf6dd486c/SKILL.md), [sci_hook.py](https://github.com/Nag681/sci-harness/blob/e241a6e930788498d87e7cc3172fe63cf6dd486c/scripts/sci_hook.py), [sci.py](https://github.com/Nag681/sci-harness/blob/e241a6e930788498d87e7cc3172fe63cf6dd486c/scripts/sci.py).
- Basis: structural bounded negative.
- Confidence: high.
- Caveats: a wider agent/human project organization may provide real S5 outside this repository's first-party workflow.

### Absence scope

- Surfaces inspected: skill rulebook, hook refusal logic, unlock/review, project task-state and installer.
- Plausible first-party paths checked: test locks as constitutional policy, human unlock reason as parent identity decision, dangerous-Git hook as S5 enforcement.
- Why no material first-party path remains: each path governs local task/command permission rather than a legitimate identity/ultimate-policy conversation with returned closure.

## Distributed OSS parent arrangement

The tool is installed into many independent agent hosts. Their local project owners and Sci-Harness maintainers do not thereby form one shared autonomous organization with a common parent closure path.

## Self-hosted and non-human modes

Installing the skill into an external agent enables a *composed* autonomous workflow. `--hooks` improves hard enforcement but does not transfer the external agent's decisive coding choices to a new first-party Sci-Harness actor.

## Recursion

Persistent tasks are sequential work labels and verification scopes, not viable autonomous sub-organizations. A host agent may recurse independently; its private topology is not inherited.

## Variety and escalation

The skill attenuates memory loss, unbounded edits and test tampering with persistent state and deterministic refusal. The host agent interprets returned `NEXT`, decides experiments and requests human clarification. STOP/ESCALATE strings are task-level control signals, not evidence that a higher VSM function owns the response.

## Evidence gaps

Static pinned-source evidence plus `python -m unittest discover -s tests -v`: **83 tests OK, 9 skipped** (platform-specific paths); no live coding-agent, model-provider, Browser or quality experiment was run. Tests establish deterministic mechanism coverage but do not prove agent organizational ownership or effectiveness. Another assessment may declare the *host-plus-installed-skill* as its system-in-focus and reach different VSM conclusions; this Index row does not silently expand its declared boundary.
