# Reflect and Update Knowledge Base Task

## Purpose
To analyze a completed session log, synthesise key learnings, and append them to the long-term knowledge base, enabling the agentic system to learn and improve over time.

## PAOA Phase: Adjust

### 1. Load and Analyze Session Log
- Read the contents of the `memory/session.log` file.
- Parse the log to identify the sequence of actions, observations (e.g., test results, QA feedback), and final outcomes.

### 2. Synthesise Learnings
- From the analysis, formulate 1-3 concise, actionable insights. Focus on:
  - **Successes**: What patterns or tool combinations were particularly effective?
  - **Failures**: What was the root cause of any errors or QA rejections?
  - **Improvements**: What could be done more efficiently in the future?

### 3. Update Knowledge Base
- Open the `memory/knowledge_base.md` file in append mode.
- Format the synthesised learnings into a new entry using the following Markdown structure:
  ```markdown
  ---
  ### Learning Entry: YYYY-MM-DD HH:MM:SS
  - **Context**: [Briefly describe the completed task, e.g., "Implemented user authentication feature."]
  - **Insight**: [State the key learning, e.g., "Using the 'security' persona during token generation successfully identified and prevented a potential vulnerability."]
  - **Actionable Change**: [Define a new rule or best practice, e.g., "Future authentication tasks should always activate the 'security' persona."]
  ```

### 4. Archive and Reset Session Log
- **(Placeholder)** In a future version, this step would archive the session log.
- For now, clear the `memory/session.log` and reset it with the initial template to prepare for the next cycle.