"""A simple planning agent."""

from __future__ import annotations

from collections.abc import Sequence

from multiple_agents.agent import Agent
from multiple_agents.message import Message


class PlannerAgent(Agent):
    """Breaks the user request into a short, ordered list of steps."""

    def __init__(self, name: str = "planner") -> None:
        super().__init__(name)

    def act(self, context: Sequence[Message]) -> Message:
        request = context[0].content
        steps = [
            f"Understand the goal: {request}",
            "Identify the inputs and constraints",
            "Produce a solution",
            "Review the result",
        ]
        plan = "\n".join(f"{i}. {step}" for i, step in enumerate(steps, start=1))
        return self._say(f"Plan:\n{plan}")
