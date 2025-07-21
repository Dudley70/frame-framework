# ORCHESTRATOR.md - SuperClaude Intelligent Routing System

Intelligent routing system for Claude Code SuperClaude framework.
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

---
## FRAME Agent and Command System

### Agent > Persona Hierarchy
- **FRAME Agents** (from BMAD) represent **roles** (e.g., dev, qa). An agent is a long-term role with specific goals.
- **SuperClaude Personas** represent temporary **specialisations** or **modes** that any agent can adopt (e.g., security, performance). A dev agent can adopt the security persona for an authentication task.

### Two-Tier Command Structure
- **/frame-tool:git**: Atomic, single-action commands for quick tasks (SuperClaude-style).
- **/frame-flow:implement**: Agentic workflow commands that trigger multi-step PAOA cycles (BMAD-style).