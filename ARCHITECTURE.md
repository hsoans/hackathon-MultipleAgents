# Hackathon System Architecture: Orchestrator & Coding Agent

## System Overview
This project uses a multi-agent design consisting of one Orchestrator Agent and one Coding Agent to build applications during a hackathon.

## Agent Definitions

### 1. Orchestrator Agent (The Manager)
* **Role**: Acts as the team lead and project planner.
* **Responsibilities**:
  * Receives the high-level hackathon idea from the human.
  * Breaks the idea down into smaller, sequential coding tasks.
  * Assigns tasks to the Coding Agent one by one.
  * Reviews the output of the Coding Agent before moving to the next task.
* **Tools**: Text planning, task tracking, and communication with the Coding Agent.

### 2. Coding Agent (The Builder)
* **Role**: Acts as the dedicated software developer.
* **Responsibilities**:
  * Receives a specific, isolated task from the Orchestrator.
  * Writes, refines, and tests the code required for that task.
  * Returns the completed code and a status report back to the Orchestrator.
* **Tools**: File system access, terminal/code execution environment, and code editing tools.

## Workflow Loop
1. Human inputs a project request -> 2. Orchestrator creates a task list 
