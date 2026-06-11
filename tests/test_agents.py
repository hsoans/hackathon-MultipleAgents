from __future__ import annotations

from multiple_agents.agents import ExecutorAgent, PlannerAgent, ReviewerAgent
from multiple_agents.cli import build_default_orchestrator, main
from multiple_agents.message import Message


def test_planner_lists_steps():
    msg = PlannerAgent().act([Message(sender="user", content="build a thing")])
    assert msg.sender == "planner"
    assert "1." in msg.content
    assert "build a thing" in msg.content


def test_executor_references_request():
    msg = ExecutorAgent().act([Message(sender="user", content="do work")])
    assert msg.sender == "executor"
    assert "do work" in msg.content


def test_reviewer_approves_when_executor_ran():
    context = [
        Message(sender="user", content="task"),
        Message(sender="executor", content="done"),
    ]
    assert "approved" in ReviewerAgent().act(context).content


def test_reviewer_flags_missing_execution():
    context = [Message(sender="user", content="task")]
    assert "needs work" in ReviewerAgent().act(context).content


def test_default_pipeline_runs_all_three_agents():
    transcript = build_default_orchestrator().run("ship it")
    senders = [m.sender for m in transcript]
    assert senders == ["user", "planner", "executor", "reviewer"]


def test_cli_main_returns_zero(capsys):
    code = main(["hello world"])
    captured = capsys.readouterr()

    assert code == 0
    assert "[planner]" in captured.out
    assert "[reviewer]" in captured.out
