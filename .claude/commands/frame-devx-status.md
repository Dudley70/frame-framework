# /frame-status Command

## Role: DevX & Observability Tool

## Purpose
To provide the user with a real-time summary of the currently active agentic workflow.

## Instructions
When this command is executed, you must perform the following actions:
1.  **Read the Session Log**: Access and read the contents of the `memory/session.log` file.
2.  **Analyze the Log**: Identify the current status of the PAOA cycle (e.g., "Planning", "Acting", "Observing") and the last few insights or actions recorded.
3.  **Report to User**: Present a concise, formatted summary to the user. Use the following template:
    
    ```markdown
    **FRAME Workflow Status**
    - **Cycle Phase**: [Current PAOA Status]
    - **Last Action**: [Describe the last action recorded in the log]
    - **Latest Insight**: [State the most recent insight from the log]
    
    *For a full history, please review the `memory/session.log` file.*
    ```
