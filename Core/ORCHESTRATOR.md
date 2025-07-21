# ORCHESTRATOR.md - FRAME Intelligent Routing System

This document guides the core LLM on how to orchestrate agents, tasks, and tools within the FRAME an agentic system that blends SuperClaude efficiency with BMAD workflows.

## 🧠 Detection Engine

Analyzes requests to understand intent, complexity, and requirements.

### Pattern Recognition Rules

#### Complexity Detection
```yaml
simple:
  indicators:
    - single file operations
    - < 3 step workflows
  token_budget: 5K

moderate:
  indicators:
    - multi-file operations
    - 3-10 step workflows
  token_budget: 15K

complex:
  indicators:
    - system-wide changes
    - > 10 step workflows
  token_budget: 30K+
```

## 🚦 Routing Intelligence

Dynamic decision trees that map detected patterns to optimal tool combinations, persona activation, and orchestration strategies.

## FRAME Agent and Command System

### Agent > Persona Hierarchy

* **FRAME Agents** (from BMAD) represent **roles** (e.g., dev, qa). An agent is a long-term role with specific goals.
* **SuperClaude Personas** represent temporary **specialisations** or **modes** that any agent can adopt (e.g., security, performance). A dev agent can adopt the security persona for an authentication task.

### Two-Tier Command Structure

* **/frame-tool:git**: Atomic, single-action commands for quick tasks (SuperClaude-style).
* **/frame-flow:implement**: Agentic workflow commands that trigger multi-step PAOA cycles (BMAD-style).

## Persona Auto-Activation System (v1.1)

Before executing a task, the Orchestrator must scan the task description and relevant context for keywords that trigger a temporary persona assignment.

### Multi-Factor Activation Scoring:

* **Keyword Matching (60%)**: Presence of specific domain keywords.
* **Task Context (40%)**: The type of agent executing and the nature of the task.

### Intelligent Activation Rules:

| Persona to Activate | Triggering Keywords | Confidence | Example Task |
|-------------------|-------------------|-----------|-------------|
| **security** | `auth`, `vulnerability`, `encryption`, `token`, `password`, `iam` | 90% | Implement JWT authentication |
| **performance** | `optimize`, `slow`, `bottleneck`, `benchmark`, `scalability`, `load` | 85% | Refactor database query for speed |
| **refactorer** | `refactor`, `cleanup`, `tech debt`, `maintainability`, `simplify` | 80% | Clean up legacy code in the payment module |
| **analyzer** | `debug`, `troubleshoot`, `investigate`, `root cause`, `error` | 95% | Find the source of a null pointer exception |