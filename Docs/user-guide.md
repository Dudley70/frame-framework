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
