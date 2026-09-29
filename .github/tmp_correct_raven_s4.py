from pathlib import Path
import re

path = Path("assessments/raven.md")
text = path.read_text(encoding="utf-8")


def replace_once(old: str, new: str, label: str) -> None:
    global text
    if old not in text:
        raise SystemExit(f"missing expected {label}")
    text = text.replace(old, new, 1)


replace_once("autonomy_s4: —", "autonomy_s4: A", "S4 frontmatter")

replace_once(
    """- System in focus: one first-party Raven Host Agent organization at pinned revision `e6c0344cb7ce00db25d554e4bb671ec1909a8f9f`, including the shared Agent Loop/Spine runtime, built-in Raven agents, host delegation and DAG machinery, Raven-Code's standard code-flow harness, permissions, session state, context/memory/skill integration, and supported user/control surfaces.""",
    """- System in focus: one first-party Raven organization at pinned revision `e6c0344cb7ce00db25d554e4bb671ec1909a8f9f`, considering both the ordinary Host Agent runtime and Raven's documented repository-shipped experimental RSI mode as distinct first-party operating modes. The boundary includes the shared Agent Loop/Spine runtime, built-in Raven agents, host delegation and DAG machinery, Raven-Code's standard code-flow harness, permissions, session state, context/memory/skill integration, supported user/control surfaces, and the generic `experimental/curator`, `experimental/analyst`, and `experimental/iteration` layers when the RSI mode is run from a source checkout.""",
    "system-in-focus line",
)
replace_once(
    """- Purpose and identity: provide a persistent host agent that can execute tasks directly or orchestrate specialized first-party and third-party agents, preserve state across turns, and expose reusable orchestration and control surfaces.""",
    """- Purpose and identity: provide a persistent host agent that can execute tasks directly or orchestrate specialized first-party and third-party agents, preserve state across turns, expose reusable orchestration and control surfaces, and, in the documented source-distribution RSI mode, revise a worker's persistent harness from evaluator feedback and execution evidence for subsequent operation.""",
    "purpose line",
)
replace_once(
    """- Standard-distribution boundary: the `raven/` runtime plus shipped agent definitions and first-party plugins under `agents/` when reached through supported launch/delegation paths. External model endpoints, MCP servers, third-party ACP/CLI/HTTP agents, remote A2A peers, EverOS service internals, and user repositories remain dependencies/environment.""",
    """- Standard-distribution boundary: the `raven/` runtime plus shipped agent definitions and first-party plugins under `agents/` when reached through supported launch/delegation paths, together with the repository-shipped `experimental/curator`, `experimental/analyst`, and `experimental/iteration` RSI path when Raven is operated from the documented source checkout. The installed wheel does not package `experimental/`, so the positive S4 mode is source-distribution-only and experimental rather than an ordinary wheel-install mode. External model endpoints, MCP servers, third-party ACP/CLI/HTTP agents, remote A2A peers, EverOS service internals, evaluator-private criteria, and user repositories remain dependencies/environment.""",
    "standard-distribution line",
)
replace_once(
    """- Credited operating / distribution surfaces: `raven/core/runtime.py`; Spine and Agent Loop; `spawn`; `run_subagent_dag`; shipped Raven-Code/Design/Oncall/PPT/Research definitions; Raven-Code code-flow tools/read ledger/Harness Manifest; task/session history; permissions; Agent-home bootstrap identity files and context assembly.""",
    """- Credited operating / distribution surfaces: `raven/core/runtime.py`; Spine and Agent Loop; `spawn`; `run_subagent_dag`; shipped Raven-Code/Design/Oncall/PPT/Research definitions; Raven-Code code-flow tools/read ledger/Harness Manifest; task/session history; permissions; Agent-home bootstrap identity files and context assembly; and, for the source-distribution RSI mode, `experimental/curator/`, `experimental/analyst/`, and `experimental/iteration/` as wired back into the real Raven AgentLoop through native extension points.""",
    "credited-surfaces line",
)
replace_once(
    """- Adjacent first-party surfaces excluded from ownership: standalone `evolver/`; benchmark suites; repository-development CI/plans; experimental simulations; documentation-only examples. They may corroborate architecture but do not become production-runtime owners.""",
    """- Adjacent first-party surfaces excluded from ownership: standalone `evolver/`; benchmark suites; repository-development CI/plans; the scenario-specific `experimental/simulation/` actors and private evaluator criteria; documentation-only examples. The generic RSI Curator/Analyst/Iteration path is credited only in its documented source-distribution mode; neighboring experiments do not donate ownership merely by repository colocation.""",
    "excluded-surfaces line",
)
replace_once(
    """- First-party operating / deployment modes considered: ordinary Host Agent turns; direct tool use; focused `spawn`; foreground/background DAGs; stateful sub-agent instances and steering; Raven-Code coding sessions; stored Playbooks executed through DAG machinery; ACP-hosted shipped agents; WebUI/TUI/RPC control.""",
    """- First-party operating / deployment modes considered: ordinary Host Agent turns; direct tool use; focused `spawn`; foreground/background DAGs; stateful sub-agent instances and steering; Raven-Code coding sessions; stored Playbooks executed through DAG machinery; ACP-hosted shipped agents; WebUI/TUI/RPC control; and the documented source-checkout RSI iteration in which Trial/Evaluator signals are analyzed and a Curator revision is validated, installed, and exercised by a later worker round.""",
    "modes line",
)
replace_once(
    """- Recursion level: one Raven Host Agent organization around a session/workspace objective. Delegated built-in agent sessions and active DAG workers are lower-recursion S1 units. Independently operated A2A peers and third-party agents remain environmental organizations.""",
    """- Recursion level: one Raven Host Agent/worker organization around a session/workspace objective. Delegated built-in agent sessions and active DAG workers are lower-recursion S1 units. In the source-distribution RSI mode, the first-party Analyst/Curator adaptation path regulates the same worker recursion by changing its future harness; it is not counted as another operational S1. Independently operated A2A peers and third-party agents remain environmental organizations.""",
    "recursion boundary line",
)

replace_once(
    """The repository's `evolver/` is intentionally outside this production boundary. Raven's own docs describe it as a standalone benchmark-driven harness-development tool; the runtime does not import it, selected candidates remain commits rather than automatically replacing the running subject, and deployment remains separate. It therefore does not donate S4 ownership to the Host Agent organization.""",
    """The repository's standalone `evolver/` remains outside the credited Host Agent/runtime boundary. Raven's own docs describe it as a benchmark-driven harness-development tool rather than a production Agent rewriting itself during ordinary operation; selected candidates remain commits and deployment is separate. It therefore is not used as the S4 witness.

Separately, the same pinned source distribution ships a documented experimental RSI path under `experimental/`. Its generic `iteration` loop runs a real worker, collects evaluator `Signal`s plus execution records, asks a model-driven Analyst for a `Feedback` decision, and on `curate` calls the model-driven Curator to revise the worker Harness. `workflow.improve` validates and installs the revision, and the next Trial executes the worker again through Raven's real AgentLoop/native extension points. Raven's README describes this as Runtime Self-Evolution, while `experimental/README.md` and `experimental/docs/rsi-iteration.md` expose the source-checkout execution path. This distinct first-party mode supplies the S4 closure credited below.""",
    "repository architecture S4 paragraph",
)

evidence_anchor = "- [`docs-site/docs/skills-and-extensions.md`](https://github.com/EverMind-AI/Raven/blob/e6c0344cb7ce00db25d554e4bb671ec1909a8f9f/docs-site/docs/skills-and-extensions.md)"
replace_once(
    evidence_anchor,
    evidence_anchor
    + "\n- [`README.md`](https://github.com/EverMind-AI/Raven/blob/e6c0344cb7ce00db25d554e4bb671ec1909a8f9f/README.md)"
    + "\n- [`CONTEXT.md`](https://github.com/EverMind-AI/Raven/blob/e6c0344cb7ce00db25d554e4bb671ec1909a8f9f/CONTEXT.md)"
    + "\n- [`experimental/README.md`](https://github.com/EverMind-AI/Raven/blob/e6c0344cb7ce00db25d554e4bb671ec1909a8f9f/experimental/README.md)"
    + "\n- [`experimental/docs/rsi-iteration.md`](https://github.com/EverMind-AI/Raven/blob/e6c0344cb7ce00db25d554e4bb671ec1909a8f9f/experimental/docs/rsi-iteration.md)",
    "primary-evidence anchor",
)

replace_once(
    """The Host Agent is the organization-level operational actor. A model-driven turn can select ordinary tools, choose specialists, submit a DAG, inspect delegated results and continue the task. Delegated built-in workers execute their own model/tool feedback loops. Constructor/runtime mechanisms such as permission gates, concurrency limits, path confinement, DAG validation, read-before-edit checks and Git-state collection constrain or verify those loops without automatically becoming agent-owned decisions.""",
    """The Host Agent is the organization-level operational actor. A model-driven turn can select ordinary tools, choose specialists, submit a DAG, inspect delegated results and continue the task. Delegated built-in workers execute their own model/tool feedback loops. Constructor/runtime mechanisms such as permission gates, concurrency limits, path confinement, DAG validation, read-before-edit checks and Git-state collection constrain or verify those loops without automatically becoming agent-owned decisions. In the documented source-distribution RSI mode, the worker remains the operational S1 while evaluator signals and execution records reach a model-driven Analyst/Curator path that chooses, validates and installs a persistent Harness revision for subsequent worker rounds.""",
    "operational model paragraph",
)

new_s4 = """## S4 — Intelligence / adaptation

- State: A
- Function: convert external evaluation of Raven worker behaviour into a prospective persistent Harness revision that changes the worker's future operating capability.
- Disturbance / variety regulated: repeated mismatch between desired behaviour/requirements and observed worker behaviour or deliverables across rounds can persist even when the current task finishes; the organization needs a path that learns from those external distinctions and changes how later work is performed.
- Decisive decision or feedback right: decide whether observed signals justify curation and, when they do, choose the concrete Harness mechanism/revision to install for the worker's next rounds.
- Decision owner: a first-party autonomous RSI path split across model-driven actors: the Analyst makes the semantic `curate` / continue / supplement / clarify / stop feedback decision from evaluator signals and execution evidence, and the Curator chooses the concrete adaptation across the worker Harness. Deterministic code validates, installs and records that decision but does not make the semantic adaptation judgment.
- Supporting / enforcement mechanisms: Trial/Evaluator protocols; `Signal` and execution/activity records; bounded Analyst exchange; Curator understand/select/design/implement/repair stages; host-owned Harness declarations/contracts; revision validation; persistent worker process; native Raven extension points; iteration state/records.
- Closure path: worker performs a Trial → evaluator returns external `Signal`s about actual behaviour/deliverables → Analyst interprets those signals plus execution evidence and can decide `curate` → Curator designs a persistent Harness revision → `workflow.improve` validates and installs it → a later Trial runs the same worker organization through the real Raven AgentLoop with the revised Harness → new behaviour is evaluated again.
- Boundary reachability: Raven documents this generic RSI mode in the pinned source distribution, ships `experimental/curator`, `experimental/analyst`, and `experimental/iteration`, exposes a source-checkout `uv run python -m experimental.iteration` entry path, and binds generated strategies through Raven's native AgentLoop extension points. The mode is explicitly experimental and not included in the installed wheel, but it is a first-party documented source-distribution operating mode rather than a repository-development benchmark actor borrowed from `evolver/`.
- External distinction: evaluation originates outside the worker's ordinary production loop: a human, dataset or scenario evaluator inspects the worker's conversations/deliverables against requirements or withheld criteria and returns `Signal`s; evaluator-private criteria are not written by the worker or Curator.
- Future / prospective distinction: the Analyst converts current-round evidence into behavioural requirements for subsequent rounds, and the Curator modifies persistent Harness strategy/configuration so later work is performed under a changed capability rather than merely retrying the same current action.
- Adaptation option generated: the Curator model can select and generate revisions across Raven's Harness strategy surfaces (Memory, Planning, Capability and Action) and connected home/config/hook/plugin/child-Harness extension points, then repair a candidate until it satisfies the host contract or fails validation.
- Path back into current capability / S3: `workflow.improve` validates and activates the selected revision in the worker, and the next Trial exercises that revision through the real Raven AgentLoop; subsequent operational evidence therefore reflects the changed present capability and can enter another adaptation round.
- Why this is / is not agent-owned: removing the model-driven Analyst/Curator actors while leaving Trial plumbing, validation, installation and persistence intact removes the semantic decision that a behaviour gap warrants curation and the choice of what organizational capability to change. The deterministic machinery enforces the selected revision but does not reproduce materially the same discretionary adaptation choice, so the supported RSI mode is `A` rather than `C`.
- Evidence: [`README.md`](https://github.com/EverMind-AI/Raven/blob/e6c0344cb7ce00db25d554e4bb671ec1909a8f9f/README.md); [`CONTEXT.md`](https://github.com/EverMind-AI/Raven/blob/e6c0344cb7ce00db25d554e4bb671ec1909a8f9f/CONTEXT.md); [`experimental/README.md`](https://github.com/EverMind-AI/Raven/blob/e6c0344cb7ce00db25d554e4bb671ec1909a8f9f/experimental/README.md); [`experimental/docs/rsi-iteration.md`](https://github.com/EverMind-AI/Raven/blob/e6c0344cb7ce00db25d554e4bb671ec1909a8f9f/experimental/docs/rsi-iteration.md).
- Basis: explicit + structural.
- Confidence: high for the documented source-distribution experimental mode; this does not claim the ordinary wheel-install mode autonomously self-evolves.
- Caveats: the S4 witness is explicitly experimental and source-checkout-only at the reviewed revision. Scenario-specific `experimental/simulation/` actors and the standalone `evolver/` are not imported as owners; they are unnecessary to establish the generic Analyst/Curator/Iteration closure.
"""
text, count = re.subn(
    r"## S4 — Intelligence / adaptation\n.*?(?=\n## S5 — Identity / ultimate policy)",
    new_s4.rstrip(),
    text,
    count=1,
    flags=re.S,
)
if count != 1:
    raise SystemExit("could not replace S4 section")

replace_once(
    """At the assessed recursion level, the Host Agent is the organization-level operational/current-control actor around one objective/session/workspace. Shipped child agents and DAG nodes can form lower-recursion S1 units. Parent/user control remains outside base recursion but is admitted where a supported first-party parent mode closes the same function, as in S3 and S5. Remote A2A peers and standalone Evolver remain separate organizations across explicit boundaries.""",
    """At the assessed recursion level, the Host Agent/worker is the organization-level operational/current-control actor around one objective/session/workspace. Shipped child agents and DAG nodes can form lower-recursion S1 units. In the documented source-distribution RSI mode, the Analyst/Curator path is an S4 metasystem function over that same worker recursion: it interprets external evaluation, chooses a Harness change, installs it, and returns the changed capability to later operation. Parent/user control remains outside base recursion but is admitted where a supported first-party parent mode closes the same function, as in S3 and S5. Remote A2A peers and standalone Evolver remain separate organizations across explicit boundaries.""",
    "recursion paragraph",
)
replace_once(
    """Raven absorbs open-ended task variety through the Host Agent model/tool loop and delegates specialized variety through the roster/DAG. Node dependencies, concurrency limits, task charters, permissions and backend capability checks reduce execution variety. Exceptions and failed results return as current-control evidence; the host can continue, replan, abandon or cancel affected work. Parent inspection/steering and ask-tier permissions supply supported escalation. Raven-Code additionally returns machine-read Git blockers through the Harness Manifest so integration decisions need not rely only on worker prose.""",
    """Raven absorbs open-ended task variety through the Host Agent model/tool loop and delegates specialized variety through the roster/DAG. Node dependencies, concurrency limits, task charters, permissions and backend capability checks reduce execution variety. Exceptions and failed results return as current-control evidence; the host can continue, replan, abandon or cancel affected work. Parent inspection/steering and ask-tier permissions supply supported escalation. Raven-Code additionally returns machine-read Git blockers through the Harness Manifest so integration decisions need not rely only on worker prose. In the source-distribution RSI mode, evaluator feedback about persistent behavioural gaps is converted into future-facing Harness revisions, adding an adaptation path for variety that ordinary current-control retries do not absorb.""",
    "variety paragraph",
)
replace_once(
    "- Evolver is present but separate and marked for planned retirement pending sign-off; that lifecycle does not alter the production-runtime S4 boundary.",
    "- Raven exposes two materially different self-improvement surfaces at the pinned revision: standalone `evolver/` remains outside the credited runtime boundary, while the documented source-distribution `experimental/curator` + Analyst/Iteration path is the positive S4 witness. The latter is explicitly experimental and not packaged in the installed wheel.",
    "S4 evidence-gap line",
)

path.write_text(text, encoding="utf-8")

sig_path = Path("data/signatures.psv")
rows = sig_path.read_text(encoding="utf-8").splitlines()
prefix = "315|raven|"
indices = [i for i, row in enumerate(rows) if row.startswith(prefix)]
if len(indices) != 1:
    raise SystemExit(f"expected exactly one Raven signature row, got {len(indices)}")
rows[indices[0]] = (
    "315|raven|Raven combines autonomous Host Agent operations with constructor-owned stale-edit coordination "
    "and machine-read Git audit, autonomous current-control plus parent steering, a source-distribution experimental "
    "RSI loop that closes S4 through model-driven Analyst/Curator harness revision and installation, and operator-owned "
    "identity/permission policy at S5."
)
sig_path.write_text("\n".join(rows) + "\n", encoding="utf-8")
