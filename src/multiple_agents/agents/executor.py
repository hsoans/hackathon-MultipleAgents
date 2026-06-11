"""A simple execution agent."""

from __future__ import annotations

from collections.abc import Sequence

from multiple_agents.agent import Agent
from multiple_agents.message import Message


class ExecutorAgent(Agent):
    """Turns the most recent plan into a (mock) executed result.

    This starter does not call an LLM; it echoes the work it would do so the
    pipeline is fully runnable and testable offline. Replace :meth:`act` with
    real tool/model calls for the hackathon.
    """

    def __init__(self, name: str = "executor") -> None:
        super().__init__(name)

    def act(self, context: Sequence[Message]) -> Message:
        request = context[0].content
        return self._say(f"Executed task for request: {request!r}")
