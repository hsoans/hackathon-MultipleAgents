"""A minimal, dependency-free multi-agent orchestration starter."""

from __future__ import annotations

from multiple_agents.agent import Agent
from multiple_agents.message import Message
from multiple_agents.orchestrator import Orchestrator

__all__ = ["Agent", "Message", "Orchestrator"]
__version__ = "0.1.0"
