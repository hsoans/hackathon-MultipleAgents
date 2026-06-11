"""A simple review agent."""

from __future__ import annotations

from collections.abc import Sequence

from multiple_agents.agent import Agent
from multiple_agents.message import Message


class ReviewerAgent(Agent):
    """Performs a trivial sanity check over prior agent output."""

    def __init__(self, name: str = "reviewer") -> None:
        super().__init__(name)

    def act(self, context: Sequence[Message]) -> Message:
        produced_work = any(msg.sender == "executor" for msg in context)
        verdict = "approved" if produced_work else "needs work: no execution found"
        return self._say(f"Review: {verdict}")
