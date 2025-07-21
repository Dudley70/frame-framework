# FRAME Core Architecture

This document outlines the technical architecture of the FRAME repository.

## Directory Structure

-   `/Core`: Contains the foundational principles and operational rules for all agents.
-   `/agents`: Defines the core agent roles (dev, qa, sm, analyst). Each agent has its own configuration and compatible personas.
-   `/tasks`: Holds specific, reusable task definitions that agents can execute.
-   `/workflows`: Contains high-level workflow definitions, like the `fullstack.yaml` for greenfield projects.
-   `/memory`: The agentic memory system.
    -   `session.log`: A temporary, YAML-structured log for the current PAOA cycle.
    -   `knowledge_base.md`: The long-term memory where agents store key learnings.
-   `/sources`: The raw, un-processed source files from SuperClaude and BMAD.
-   `/setup`: Contains the main `installer.py` script.
-   `/tests`: Unittests for the framework.
-   `/.claude/commands`: Holds the definitions for the two-tier slash commands.

## The Installer

The `setup/installer.py` script is responsible for:
1.  Copying the core principles from `sources/superclaude`.
2.  Copying and configuring the agents, tasks, and workflows from `sources/bmad`.
3.  Injecting the `compatible_personas` YAML frontmatter into agent files.
4.  Creating the two-tier command structure in `/.claude/commands`.
5.  Initialising the `memory/` directory with its templates.