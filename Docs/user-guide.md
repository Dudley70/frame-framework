# FRAME User Guide

Welcome to the **Framework for Responsive Agentic Modular Engineering (FRAME)**.

## Quick Start

1.  **Installation**: Run the installer to set up the FRAME environment.
    ```bash
    python3 setup/installer.py
    ```

2.  **Explore Commands**: FRAME uses a two-tier command system.
    -   **Tools**: For quick, atomic actions.
        ```bash
        /frame-tool:git status 
        ```
    -   **Flows**: To initiate complex, multi-step agentic workflows.
        ```bash
        /frame-flow:implement --story=STORY-123
        ```

## Core Concepts

### Agent > Persona Hierarchy
-   **Agents** are persistent roles (e.g., `dev`, `qa`).
-   **Personas** are temporary specialisations an agent can adopt (e.g., `security`, `performance`).

### The PAOA Cycle
FRAME agents operate on a **Plan-Act-Observe-Adjust (PAOA)** cognitive cycle. A `/frame-flow` command kicks off this loop, where agents will:
1.  **Plan** the work based on the story.
2.  **Act** by generating code and running tools.
3.  **Observe** the results via tests and validation.
4.  **Adjust** the plan based on observations, storing key learnings in the `memory/knowledge_base.md`.