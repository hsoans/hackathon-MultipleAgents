"""Command-line entrypoint for the multi-agent starter."""

from __future__ import annotations

import argparse
from collections.abc import Sequence

from multiple_agents.agents import ExecutorAgent, PlannerAgent, ReviewerAgent
from multiple_agents.orchestrator import Orchestrator


def build_default_orchestrator() -> Orchestrator:
    """Create an orchestrator wired with the bundled example agents."""
    return Orchestrator([PlannerAgent(), ExecutorAgent(), ReviewerAgent()])


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="multiple-agents",
        description="Run the example multi-agent pipeline on a request.",
    )
    parser.add_argument(
        "request",
        nargs="?",
        default="Say hello to the hackathon",
        help="The task/request to hand to the agents.",
    )
    args = parser.parse_args(argv)

    orchestrator = build_default_orchestrator()
    transcript = orchestrator.run(args.request)
    for message in transcript:
        print(message)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
