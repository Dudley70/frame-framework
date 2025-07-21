# Automated QA Review Task

## Purpose
To autonomously review a story marked as complete by the 'dev' agent, execute validation checks, and either approve it or create sub-tasks for remediation.

## PAOA Phase: Observe

### 1. Initialise Review
- Load the target story file provided by the Orchestrator.
- Verify the story status is "Review".

### 2. Execute Validation Gates
- **Gate 1: Checklist Compliance**: Programmatically execute the 'checklists/story-dod-checklist.md'. All items must be checked.
- **Gate 2: Automated Testing**: Execute the project's test suite (e.g., using an MCP tool like Playwright or running a command like \`python -m unittest\`). All tests must pass.
- **Gate 3: Code Quality Scan**: (Placeholder) Perform a static analysis scan for code quality issues.

### 3. Analyse Results and Decide
- **If all gates pass**:
  1. Update the story status to "Done".
  2. Add a success entry to the 'memory/session.log'.
  3. Proceed to the "Reflect and Update KB" task.
- **If any gate fails**:
  1. Update the story status to "InProgress_QA_Failed".
  2. Document the specific failure (e.g., "DoD item 'Testing' incomplete", "Unit test 'test_auth.py' failed.") in the story's QA section.
  3. Create a new, specific sub-task for the 'dev' agent detailing the required fix.
  4. Add a failure entry to the 'memory/session.log'.
