# FRAME User Guide (v1.1)

Welcome to the **Framework for Responsive Agentic Modular Engineering (FRAME)**. This guide explains how to use the core features of the v1.1 release.

## Quick Start

1.  **Installation**: Run the installer from your project's root directory to set up the FRAME environment.
    ```bash
    python3 setup/installer.py
    ```

2.  **Explore Commands**: FRAME uses a two-tier command system for the Claude Code IDE.
    -   **Tools**: For quick, single-shot actions.
        ```bash
        /frame-tool:git status 
        ```
    -   **Flows**: To initiate complex, multi-step agentic workflows that run autonomously.
        ```bash
        /frame-flow:implement --story=STORY-123
        ```

## Core Concepts

### Agent > Persona Hierarchy
FRAME uses a sophisticated model for its AI workforce:
-   **Agents** are persistent roles with specific goals (e.g., the `dev` agent's goal is to implement code).
-   **Personas** are temporary specialisations or "modes" an agent can adopt based on context (e.g., the `dev` agent automatically adopts the `security` persona when working on authentication code).

### The PAOA Cycle (Plan-Act-Observe-Adjust)
FRAME agents operate on a cognitive cycle. When you trigger a `/frame-flow`, the agentic system will:
1.  **Plan** the work required to complete the task.
2.  **Act** by generating code, running tests, and using tools.
3.  **Observe** the results via the automated QA loop and self-correction.
4.  **Adjust** by reflecting on the outcome, updating its knowledge base for future tasks, and creating sub-tasks if needed.

### New in v1.1: Check Agent Status
You can get a quick snapshot of what an agent is doing during a long-running `/frame-flow` by using the status command:
```bash
/frame-status
```

## 4.0 Structured Project Management in FRAME
For projects that span multiple sessions, FRAME incorporates a structured project management methodology to ensure context is never lost and development remains focused. This methodology is built on three key documents:
1.  **The Master Development Brief**: The long-term strategic plan for the entire project. It contains the full roadmap, technical specifications for all phases, and core architectural principles.
2.  **The Task Specification**: A granular, tactical plan for a single User Story. It breaks down the task into precise technical steps and is used to generate prompts for the AI agent.
3.  **The Handover Document**: A point-in-time snapshot created at the end of a work session. It captures the final state of the project and defines the objective for the next session.
This approach provides a robust and repeatable process, taking you cleanly from high-level strategy to low-level, AI-driven execution.
