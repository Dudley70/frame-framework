# FRAME Concept Proposal: C001 - Multi-LLM Agent Orchestration

**Date:** 2025-07-22
**Status:** Under Review

---

### 1. The Idea
To enable FRAME to dynamically use different large language models (e.g., Gemini, Claude) for different tasks or agents within a single workflow, without the user having to switch interfaces.

### 2. The Rationale (The "Why")
Different models excel at different tasks. For example:
* **Gemini** might be superior for creative ideation, planning, and specification generation.
* **Claude** might be preferred for precise, high-quality code generation.

By allowing the right model to be used for the right job, we significantly increase the overall quality and efficiency of the agentic system. This aligns with FRAME's vision of being a powerful, best-in-class toolkit.

### 3. Proposed Implementation (The "How")
This would require architectural changes:
* **Core Abstraction**: Create a generic "LLM Provider" interface in the FRAME Core. Concrete implementations would be created for each supported model (e.g., `ClaudeProvider`, `GeminiProvider`).
* **Configuration**: Update `frame.config.yaml` to allow users to define a default model and specify model overrides for specific agents or tasks.
    ```yaml
    llm:
      default_provider: claude
      task_overrides:
        - task: "generate-spec.md"
          provider: gemini
        - agent: "dev-agent"
          provider: claude-3.5
    ```
* **Adapter Update**: The VS Code Adapter would need to be updated to route requests to the correct model's API based on the configuration.

### 4. Strategic Fit & Priority
This is a significant architectural enhancement. It would likely fit into **Phase 3 (Ecosystem & Scalability)** or **Phase 4 (Exploratory)**, as it builds on the core modularity of the system.
