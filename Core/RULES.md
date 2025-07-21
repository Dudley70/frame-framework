# RULES.md - SuperClaude Framework Actionable Rules

Simple actionable rules for Claude Code SuperClaude framework operation.
## Core Operational Rules

### Task Management Rules
- TodoRead() → TodoWrite(3+ tasks) → Execute → Track progress
- Use batch tool calls when possible, sequential only when dependencies exist
- Always validate before execution, verify after completion

### File Operation Security
- Always use Read tool before Write or Edit operations
- Use absolute paths only, prevent path traversal attacks

### Framework Compliance
- Check package.json/pyproject.toml before using libraries
- Follow existing project patterns and conventions

### Systematic Codebase Changes
- **MANDATORY**: Complete project-wide discovery before any changes
- Verify completion with comprehensive post-change search
- Validate related functionality remains working

---
## FRAME Quality Assurance Rules (from BMAD DoD)
- **Requirements Met**: All functional requirements and acceptance criteria must be implemented.
- **Coding Standards**: All code must adhere to project coding standards and structure.
- **Testing**: All required unit and integration tests must be implemented and passing.
- **Verification**: Functionality must be manually verified by the developer.
- **Story Administration**: All tasks in the story file must be marked as complete.
- **Dependencies**: Any new dependencies must be approved and documented.