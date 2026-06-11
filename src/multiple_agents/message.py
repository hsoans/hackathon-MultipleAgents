"""Lightweight message type passed between agents."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import UTC, datetime


@dataclass(frozen=True)
class Message:
    """A single unit of communication in the shared context.

    Attributes:
        sender: Name of the agent (or "user") that produced the message.
        content: The textual payload.
        created_at: UTC timestamp of creation.
    """

    sender: str
    content: str
    created_at: datetime = field(default_factory=lambda: datetime.now(UTC))

    def __str__(self) -> str:
        return f"[{self.sender}] {self.content}"
