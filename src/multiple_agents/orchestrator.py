"""Coordinates a sequence of agents over a shared context."""

from __future__ import annotations

from collections.abc import Iterable

from multiple_agents.agent import Agent
from multiple_agents.message import Message


class Orchestrator:
    """Runs registered agents in order, accumulating a shared transcript.

    Each agent sees every message produced before it (including the original
    request and earlier agents' output), then appends its own contribution.
    """

    def __init__(self, agents: Iterable[Agent]) -> None:
        self.agents: list[Agent] = list(agents)
        self.context: list[Message] = []

    def run(self, request: str) -> list[Message]:
        """Run a single pass over all agents for the given request.

        Returns the full transcript, starting with the user request.
        """
        self.context = [Message(sender="user", content=request)]
        for agent in self.agents:
            self.context.append(agent.act(self.context))
        return list(self.context)

    @property
    def result(self) -> Message | None:
        """The last message produced, or ``None`` if nothing has run."""
        return self.context[-1] if self.context else None
