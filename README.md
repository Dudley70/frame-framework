# FRAME: Framework for Responsive Agentic Modular Engineering

**FRAME** is an agentic AI development toolkit that blends SuperClaude's efficient extensions with BMAD's structured workflows for Claude Code.

## Quick Start

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Dudley70/frame-framework.git
   cd frame-framework
   ```

2. **Run the installer**:
   ```bash
   python3 setup/installer.py
   ```

3. **Start using FRAME commands**:
   - **Tools**: `/frame-tool:git status` (atomic actions)
   - **Flows**: `/frame-flow:implement` (multi-step workflows)

## Architecture

FRAME combines the best of two worlds:

- **SuperClaude**: Efficient, token-optimized operations with evidence-based reasoning
- **BMAD**: Structured agentic workflows with specialized roles and PAOA cycles

### Core Components

- **`/Core`**: Foundational principles, rules, and orchestration
- **`/agents`**: Specialized AI agents (analyst, dev, qa, sm)
- **`/tasks`**: Reusable task definitions
- **`/workflows`**: High-level process templates
- **`/memory`**: Persistent knowledge and session tracking

## Documentation

- [User Guide](Docs/user-guide.md) - Complete usage instructions
- [Architecture](Docs/core-architecture.md) - Technical deep-dive

## Testing

Run the test suite to verify installation:

```bash
python3 -m unittest discover tests
```

## Version

Current version: **1.0.0**

---

**FRAME** transforms you into a "Vibe CEO" - directing specialized AI agents through proven development workflows while maintaining SuperClaude's efficiency principles.
