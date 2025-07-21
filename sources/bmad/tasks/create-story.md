# Create Next Story Task

## Purpose
To identify the next logical story based on project progress and epic definitions, and then to prepare a comprehensive, self-contained, and actionable story file.

## SEQUENTIAL Task Execution

### 1. Identify Next Story for Preparation
- Locate epic files based on prdSharded config.
- Review existing stories in devStoryLocation.
- If no stories exist, the next story is 1.1.

### 2. Gather Story Requirements and Context
- Extract requirements from the identified epic file.
- Review previous story's Dev Agent Record for insights.

### 3. Gather Architecture Context
- Read relevant sharded architecture documents based on story type (Backend, Frontend, Full-stack).
- Extract story-specific technical details with source citations.

### 4. Populate Story Template
- Create new story file: {devStoryLocation}/{epicNum}.{storyNum}.story.md.
- Populate Dev Notes with all technical context from architecture docs.
- Generate a detailed, sequential list of technical tasks in Tasks / Subtasks.