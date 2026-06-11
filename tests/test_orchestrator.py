from __future__ import annotations

from collections.abc import Sequence

from multiple_agents import Agent, Message, Orchestrator


class EchoAgent(Agent):
    def act(self, context: Sequence[Message]) -> Message:
        return self._say(f"echo:{context[0].content}")


def test_run_records_user_request_first():
    orch = Orchestrator([EchoAgent("a")])
    transcript = orch.run("hello")

    assert transcript[0].sender == "user"
    assert transcript[0].content == "hello"


def test_run_appends_each_agent_in_order():
    orch = Orchestrator([EchoAgent("a"), EchoAgent("b")])
    transcript = orch.run("hi")

    assert [m.sender for m in transcript] == ["user", "a", "b"]
    assert transcript[-1].content == "echo:hi"


def test_result_is_last_message():
    orch = Orchestrator([EchoAgent("a")])
    assert orch.result is None

    orch.run("x")
    assert orch.result is not None
    assert orch.result.sender == "a"


def test_run_is_idempotent_per_call():
    orch = Orchestrator([EchoAgent("a")])
    first = orch.run("one")
    second = orch.run("two")

    assert len(first) == len(second) == 2
    assert second[0].content == "two"
