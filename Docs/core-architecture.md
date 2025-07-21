# FRAME Core Architecture (v1.1)

This document outlines the technical architecture of the FRAME repository.

## Directory Structure

-   `/Core`: Foundational principles, rules, and the **Orchestrator** logic. The Orchestrator now includes logic for **Dynamic Persona** loading.
-   `/agents`: Defines the core agent roles (dev, qa, sm, analyst). Each agent has its own configuration and a list of compatible personas.
-   `/tasks`: Reusable task definitions. Now includes the **automated-qa-review.md** and **reflect-update-kb.md** tasks.
-   `/workflows`: High-level YAML workflow definitions. The `fullstack.yaml` now includes the **automated QA loop**.
-   `/memory`: The agentic memory system, containing a session log and the long-term knowledge base.
-   `/config`: Contains the modular `features.json` that the installer uses to register components.
-   `/setup`: Contains the main `installer.py` script, now refactored to be modular.
-   `/tests`: The `unittest` suite for the framework.
-   `/.claude/commands`: Holds the definitions for the two-tier slash commands, including the new `/frame-status` command.

## Key Architectural Features of v1.1

-   **Extended Installer**: The installer now reads component definitions from `config/features.json`, allowing for modular and scalable installation of new agents and tasks.
-   **Automated QA Loop**: The main workflow now contains a closed loop where the `dev` agent's output is automatically passed to the `qa` agent. The `qa` agent executes an automated review task, and can create sub-tasks for the `dev` agent if validation fails.
-   **Memory & Reflection System**: After a QA cycle, agents use the `reflect-update-kb.md` task to parse the `memory/session.log` and store permanent learnings in the `memory/knowledge_base.md`, enabling the system to improve over time.
