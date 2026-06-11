# hackathon-MultipleAgents

A minimal, dependency-free **multi-agent orchestration** starter for the hackathon.

It ships a tiny, fully runnable example pipeline — `PlannerAgent → ExecutorAgent → ReviewerAgent`
coordinated by an `Orchestrator` over a shared message transcript. There are no LLM/API calls,
so everything runs and tests offline; swap each agent's `act()` for real model/tool calls as you build.

## Requirements

- Python 3.11+
- [uv](https://docs.astral.sh/uv/) (recommended) — or plain `pip`

## Setup

```bash
uv sync --extra dev      # create .venv and install runtime + dev deps
```

Using pip instead:

```bash
python -m venv .venv && source .venv/bin/activate
pip install -e ".[dev]"
```

## Run

```bash
uv run multiple-agents "Summarize the repo"
# or, without installing the script:
uv run python -m multiple_agents.cli "Summarize the repo"
```

## Develop

```bash
uv run ruff check src tests     # lint
uv run ruff check --fix src tests
uv run pytest                   # run tests
```

## Layout

```
src/multiple_agents/
  agent.py          # Agent ABC (implement act())
  message.py        # Message dataclass (shared-context unit)
  orchestrator.py   # Orchestrator: runs agents in order over a transcript
  cli.py            # `multiple-agents` entrypoint
  agents/           # Example PlannerAgent / ExecutorAgent / ReviewerAgent
tests/              # pytest suite
```

## Add your own agent

```python
from collections.abc import Sequence
from multiple_agents import Agent, Message, Orchestrator

class ShoutAgent(Agent):
    def act(self, context: Sequence[Message]) -> Message:
        return self._say(context[0].content.upper())

Orchestrator([ShoutAgent("shout")]).run("hello")
```
