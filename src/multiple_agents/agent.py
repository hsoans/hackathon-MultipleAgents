"""Base agent abstraction."""

from __future__ import annotations

from abc import ABC, abstractmethod
from collections.abc import Sequence

from multiple_agents.message import Message


class Agent(ABC):
    """Abstract base class for an agent.

    Subclasses implement :meth:`act`, which receives the running transcript
    (shared context) and returns this agent's contribution.
    """

    def __init__(self, name: str) -> None:
        self.name = name

    @abstractmethod
    def act(self, context: Sequence[Message]) -> Message:
        """Produce a message given the shared context so far."""
        raise NotImplementedError

    def _say(self, content: str) -> Message:
        """Helper to build a Message attributed to this agent."""
        return Message(sender=self.name, content=content)

    def __repr__(self) -> str:
        return f"{type(self).__name__}(name={self.name!r})"
