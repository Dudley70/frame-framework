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