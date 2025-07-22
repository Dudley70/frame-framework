# FRAME Master Development Brief

**Version**: 1.2.0

**Last Updated**: 2025-07-22

## 1.0 Executive Summary & Strategic Overview

### 1.1. Project Vision

To build FRAME into a leading open-source agentic development toolkit that is powerful, portable, observable, and safe. FRAME enables developers to build, test, and deploy specialised AI agents by synthesising the best patterns from foundational frameworks and the broader AI ecosystem. By blending SuperClaude's efficient Claude Code extensions with BMAD's agentic agile workflows, FRAME creates a responsive, modular system focused on PAOA cycles, hierarchical orchestration, and seamless Claude Code integration. The vision emphasizes ethical autonomy, hybrid human-AI collaboration, and extensibility for 2025 trends like multi-agent systems and edge AI.

### 1.2. The FRAME Blueprint: An Analogy

To understand FRAME's relationship with its foundational frameworks, think of it like building a new, custom car 🚗:

* **SuperClaude** is the proven, reliable engine we've selected for its efficiency and power within the Claude ecosystem.
* **BMAD** is the advanced, agile chassis design we've adopted for its structured, multi-agent approach to handling complex tasks.
* **FRAME** is the new, custom car we are building by integrating this engine and chassis.

This Master Development Brief is the detailed engineering blueprint for our new car. It is specific to FRAME and describes exactly how we are assembling our unique vehicle. It does not change the original engine's design (SuperClaude) or the original chassis schematics (BMAD) in any way. They are the respected inspirations; this is the plan for our new creation.

### 1.3. Prioritised Roadmap Overview

* 🚀 **High Priority: Phase 1 & 2 (Foundations, Governance & Core DevX)**: Deliver a stable, observable, and safe Version 1.2 with a VS Code adapter.
* 🛠️ **Medium Priority: Phase 3 (Ecosystem & Advanced Features)**: Grow FRAME from a tool into a platform by enabling community contributions and specialisations.
* 🔬 **Low Priority: Phase 4 & 5 (Future-Proofing & Productisation)**: Explore cutting-edge capabilities and prepare the project for long-term, sustainable management.

**Estimated Timeline (Assuming 3 Devs, 20h/week)**: Phase 1-2: 4-8 weeks; Phase 3: 2-4 weeks; Phase 4-5: 3-6 months post-MVP. Total: 10-18 weeks to v2.0.

**Success Metrics/KPIs**: GitHub stars >1K in 6 months; test coverage >80%; NPS >8/10 from issues; zero high-severity security incidents; agent self-correction success rate >85%.

**Risks & Mitigations**:

* **Instability (e.g., n8n changes)**: Mitigate with version pinning/tests (High).
* **Scope Creep**: Use RICE/MoSCoW scoring monthly (Medium).
* **Adoption**: Community onboarding via docs/tutorials (Low).
* **Tech Debt**: Automated scans (Semgrep) in CI/CD (High).

### 1.4. Core Architectural Principles

* **Core and Adapter Model**: The FRAME Core (agnostic logic) is decoupled from IDE Adapters (specific integrations) via a defined protocol.
* **Tiered Knowledge Strategy**: Agent expertise is built in layers: Embedded Knowledge (Tier 1), Embedded Skills (Tier 2), and Live Augmentation (Tier 3).
* **Open-Source Native Tooling**: Prioritise using standard, well-supported open-source tools to accelerate development and ensure maintainability.
* **Ethical Autonomy by Design**: Integrate governance (e.g., NIST RMF) and privacy (e.g., GDPR checks) from the start.
* **Hybrid Human-AI Focus**: Emphasize HITL and intuitive UIs for collaboration.
* **Modular Extensibility**: Design for easy expansions via manifests and marketplaces.

## 2.0 Phase-by-Phase Technical Specifications

### 🚀 Phase 1 & 2: Foundations, Governance & Core DevX (High Priority)

#### Theme: Core Architecture & Portability

* **Epic 1: Implement a Portable and Scalable Core Architecture**
    * **User Story/Issue #101: Define Hybrid AI Comms Protocol**
        * **Status**: Not Started
        * **Goal**: Establish a robust and performant communication protocol between the FRAME Core and its adapters.
        * **AC**: The protocol must support AI-native features like tool discovery and provide a reliable fallback.
        * **Implementation Plan**:
            * Define the primary protocol using MCP (Model Context Protocol) for its AI-native features.
            * Define a JSON-RPC 2.0 specification as a reliable fallback for non-AI adapters.
            * Investigate GraalVM for native bindings to reduce language-specific code and enhance security for polyglot communication.
        * **Dependencies**: Core ORCHESTRATOR.md; n8n REST API for inspiration.
        * **Effort Estimate**: 1-2 weeks; Tests: Unit for API calls, integration for MCP/JSON-RPC.
        * **Metrics**: Latency <100ms; 100% coverage for error handling.

    * **User Story/Issue #102: Architect for Headless & Cloud Deployment**
        * **Status**: Not Started
        * **Goal**: Ensure the core agentic engine can run independently of any desktop UI, ready for team and cloud environments.
        * **AC**: The FRAME Core must be fully containerisable and expose its services exclusively via the defined API. All user-specific state must be handled externally.
        * **Implementation Plan**:
            * Refactor the Core to be completely stateless.
            * Develop a clear multi-tenancy model where each API request includes a project/user ID to isolate contexts.
            * Use Firecracker microVMs as the target architecture for secure, high-performance sandboxing of cloud-based agents.
        * **Dependencies**: Docker/Podman setup; Redis for state (via n8n queue mode).
        * **Effort Estimate**: 1 week; Tests: Container build/deploy sims.
        * **Metrics**: Startup time <200ms; supports 10+ concurrent users.

    * **User Story/Issue #103: Implement Defensive n8n Backend Integration**
        * **Status**: Not Started
        * **Goal**: Safely leverage n8n for workflow automation without exposing FRAME to its potential instability.
        * **AC**: n8n must run in a controlled, self-hosted environment with pinned versions.
        * **Implementation Plan**:
            * Create a docker-compose.yaml to run a self-hosted n8n instance.
            * Use Valkey (the open-source Redis fork) to enable n8n's scalable queue mode.
            * Establish a secure REST API for triggering n8n workflows from FRAME.
        * **Dependencies**: n8n v1.102.4; CI/CD pipeline.
        * **Effort Estimate**: 1 week; Tests: Regression suite for n8n upgrades.
        * **Metrics**: Workflow throughput >100/min; zero breaking changes impact.

#### Theme: Integrated Governance, Security, and Process Framework

* **Epic 2: Establish a Professional Development Lifecycle**
    * **User Story/Issue #201: Formalise the Project & Documentation Lifecycle**
        * **Status**: Not Started
        * **Goal**: Implement a formal, auditable process for managing all project documentation and planning.
        * **AC**: The methodology must be implemented using the Master_Development_Brief.md, Task_Specification_Template.md, and Handover_Template.md.
        * **Implementation Plan**:
            * Integrate MLflow for AI-specific lifecycle management to track experiments, workflows, and models.
            * Align templates with principles from PMBOK (Risk/Quality), PRINCE2 (Staged Management), and BABOK (Requirements Analysis).
        * **Dependencies**: GitHub templates; MLflow integration.
        * **Effort Estimate**: 1 week; Tests: Template validation scripts.
        * **Metrics**: 100% process coverage; monthly reviews logged.

    * **User Story/Issue #202: Implement the Elicitation Process**
        * **Status**: Not Started
        * **Goal**: To resolve ambiguities in feature concepts before development begins.
        * **AC**: An "Analyst Agent" must use the tasks/clarify-concept-proposal.md task to refine a Concept Proposal.
        * **Implementation Plan**:
            * Enhance the process with a multi-agent system using CrewAI for its strong task delegation and HITL capabilities.
        * **Dependencies**: Analyst agent from BMAD; clarify-concept-proposal.md.
        * **Effort Estimate**: 1 week; Tests: Dialogue sims.
        * **Metrics**: Ambiguity resolution rate >90%.

    * **User Story/Issue #203: Implement a Dynamic Prioritisation Process**
        * **Status**: Not Started
        * **Goal**: To ensure the project remains agile and focused on the highest-impact features.
        * **AC**: A formal process for scoring and ranking feature proposals must be in place.
        * **Implementation Plan**:
            * Adopt the MoSCoW (Must, Should, Could, Won't) method for prioritisation.
            * Use a tool like Airtable to manage the feature backlog and scoring.
        * **Dependencies**: GitHub issues; monthly review cadence.
        * **Effort Estimate**: 0.5 weeks; Tests: Scoring automation.
        * **Metrics**: Backlog health score >80%.

* **Epic 3: Build a Unified Security & Compliance Framework**
    * **User Story/Issue #301: Integrate Security & Compliance Standards**
        * **Status**: Not Started
        * **Goal**: To build a trustworthy, enterprise-ready framework that is secure by design.
        * **AC**: The framework must have foundational alignment with ISO 27001, ISO 42001, and the NIST AI RMF.
        * **Implementation Plan**:
            * Use Semgrep in the CI/CD pipeline for fast, AI-aware static analysis.
            * Integrate Guardrails AI for runtime compliance checks on agent outputs.
        * **Dependencies**: CI/CD (GitHub Actions); Semgrep config.
        * **Effort Estimate**: 1-2 weeks; Tests: Vulnerability scans.
        * **Metrics**: Zero high-severity issues; compliance score >90%.

    * **User Story/Issue #302: Implement Data Governance and Privacy by Design**
        * **Status**: Not Started
        * **Goal**: To build user trust and ensure compliance with global privacy regulations.
        * **AC**: A formal Data_Handling_Policy.md and a process for Privacy Impact Assessments (PIAs) must be established.
        * **Implementation Plan**:
            * Establish the data handling policy and PIA process.
            * Use tools from the OpenDP project to explore implementing differential privacy for agent telemetry.
        * **Dependencies**: Data_Handling_Policy.md template; OneTrust alternative for automated PIAs.
        * **Effort Estimate**: 1 week; Tests: PIA sims.
        * **Metrics**: 100% features with PIAs; privacy incidents = 0.

#### Theme: Core Agent Autonomy & DevX

* **Epic 4: Implement Advanced Autonomy and User Experience**
    * **User Story/Issue #401: Implement Multi-Layered Guardrails & HITL**
        * **Status**: Not Started
        * **Goal**: To provide comprehensive safety and control, making the system fundamentally safe to operate.
        * **AC**: The system must have mechanisms to prevent loops, allow human intervention, and securely sandbox code.
        * **Implementation Plan**:
            * Use LangGraph for its powerful, graph-based control over agentic loops and HITL workflows.
            * Use Firecracker for secure, high-performance microVM sandboxing of agent-generated code.
        * **Dependencies**: CrewAI fallback; Podman alternative.
        * **Effort Estimate**: 1 week; Tests: Loop detection sims.
        * **Metrics**: Guardrail activation success >95%.

    * **User Story/Issue #402: Implement Real-Time Observability Dashboard**
        * **Status**: Not Started
        * **Goal**: To solve the agent "black-box" problem with a production-ready, open-source solution.
        * **AC**: The VS Code adapter must display a real-time dashboard showing agent traces, timelines, and thoughts.
        * **Implementation Plan**:
            * Integrate the open-source Langfuse SDK to provide a production-ready dashboard inside a VS Code webview.
        * **Dependencies**: Lunary/Phoenix alternative for affordability/UI.
        * **Effort Estimate**: 1 week; Tests: Streaming sims.
        * **Metrics**: Latency visualization accuracy 100%.

    * **User Story/Issue #403: Implement Interactive Intervention Workflow**
        * **Status**: Not Started
        * **Goal**: To empower the developer as a true collaborator with the AI agent.
        * **AC**: The observability dashboard must include Pause, Resume, and Cancel buttons, and a way to provide corrective feedback.
        * **Implementation Plan**:
            * Use LangGraph or CrewAI to manage the state and logic for these human interventions.
        * **Dependencies**: Semantic Kernel for natural language input.
        * **Effort Estimate**: 1 week; Tests: Pause/resume flows.
        * **Metrics**: Intervention success rate >90%.

    * **User Story/Issue #404: Implement Voice-Powered Ideation Workflow**
        * **Status**: Not Started
        * **Goal**: To provide a superior user experience for the creative process of brainstorming new ideas.
        * **AC**: A user must be able to speak an idea and have the system generate a populated Concept_Proposal_Template.md.
        * **Implementation Plan**:
            * Use a best-in-class transcription service like AssemblyAI or Deepgram for high-accuracy voice capture within the VS Code webview.
        * **Dependencies**: Web Speech API fallback; Ideation Agent.
        * **Effort Estimate**: 1 week; Tests: Transcription accuracy >95%.
        * **Metrics**: Proposal generation time <30s.

### **🛠️ Medium Priority: Phase 3 (Ecosystem & Advanced Features)**

* **Epic 5: Enhance Agent Intelligence**
    * **User Story/Issue #501: Implement Self-Correcting PAOA Loops**
        * **Status**: Not Started
        * **Goal**: Enhance agent autonomy with multi-agent correction.
        * **AC**: Locator/Fixer team with patch generation.
        * **Implementation Plan**:
            * Use frameworks like AutoGen for coordination. The Fixer agent will use patch generation techniques from research like GiantRepair.
        * **Dependencies**: CrewAI/LangGraph alternative.
        * **Effort Estimate**: 1-2 weeks; Tests: Correction sims.
        * **Metrics**: Success rate >85%.

    * **User Story/Issue #502: Implement Dynamic Tool Generation**
        * **Status**: Not Started
        * **Goal**: Allow agents to create/execute tools on-the-fly.
        * **AC**: Tool Factory in secure sandbox.
        * **Implementation Plan**:
            * Create the "Tool Factory" agent that can generate and execute its own scripts in a secure Podman sandbox.
        * **Dependencies**: Firecracker/QEMU alternative.
        * **Effort Estimate**: 1 week; Tests: Sandbox security.
        * **Metrics**: Tool creation time <1min.

    * **User Story/Issue #503: Implement Pluggable Multi-LLM Orchestration**
        * **Status**: Not Started
        * **Goal**: Use optimal LLMs per task.
        * **AC**: Generic interface configured in yaml.
        * **Implementation Plan**:
            * Implement a generic "LLM Provider" interface, allowing the framework to use the best model (e.g., Gemini for ideation, Claude for code) for each task, configured via frame.config.yaml.
        * **Dependencies**: Haystack/DSPy for orchestration.
        * **Effort Estimate**: 1 week; Tests: Model switching.
        * **Metrics**: Response quality improvement >20%.

* **Epic 6: Build the Community Ecosystem**
    * **User Story/Issue #601: Launch Expansion Packs Marketplace via GitHub**
        * **Status**: Not Started
        * **Goal**: Hub for community extensions.
        * **AC**: Manifest-based discovery/rating.
        * **Implementation Plan**:
            * Formalise the frame-expansion.json manifest and leverage the existing GitHub Marketplace infrastructure to create a hub for discovering, rating, and installing community-built extensions.
        * **Dependencies**: Hugging Face alternative for AI packs.
        * **Effort Estimate**: 1 week; Tests: Install flows.
        * **Metrics**: >100 packs in 6 months.

    * **User Story/Issue #602: Implement Secure Plugin Runtime with MicroVMs**
        * **Status**: Not Started
        * **Goal**: Safe execution for plugins.
        * **AC**: Sandboxed with permissions.
        * **Implementation Plan**:
            * Use Firecracker and GraalVM to provide state-of-the-art, sandboxed execution for community-contributed plugins, ensuring they cannot compromise the user's system.
        * **Dependencies**: QEMU/Kata alternative.
        * **Effort Estimate**: 1 week; Tests: Malware sims.
        * **Metrics**: Zero breaches.

* **Epic 7: Enable Team Collaboration**
    * **User Story/Issue #701: Implement Collaborative Team Workflows**
        * **Status**: Not Started
        * **Goal**: Multi-user support.
        * **AC**: Shared dashboard and RBAC.
        * **Implementation Plan**:
            * Design the features needed for multiple users to collaborate, including a shared web-based project dashboard and leveraging the ROLES.md for role-based access control.
        * **Dependencies**: Budibase for low-code dashboard.
        * **Effort Estimate**: 1-2 weeks; Tests: Multi-user sims.
        * **Metrics**: Concurrent users >5.

### **🔬 Low Priority: Phase 4 & 5 (Future-Proofing & Productisation)**

* **Epic 8: Transition to Product Lifecycle Management (PLM)**
    * **User Story/Issue #801: Formalise Release Management and Support Processes**
        * **Status**: Not Started
        * **Goal**: Sustainable management.
        * **AC**: SemVer, bug triage, deprecation policy.
        * **Implementation Plan**:
            * Formalise processes for Semantic Versioning (SemVer), bug reporting and triage (BUG_REPORT.md template), and a transparent feature Deprecation Policy.
        * **Dependencies**: MLflow/Neptune.ai for AI PLM.
        * **Effort Estimate**: 1 week; Tests: Release sims.
        * **Metrics**: Release cycle <2 weeks.

* **Epic 9: Explore Advanced Reasoning Capabilities**
    * **User Story/Issue #901: Implement Advanced RAG with Hybrid Search**
        * **Status**: Not Started
        * **Goal**: Sophisticated knowledge reasoning.
        * **AC**: Hybrid vector/graph integration.
        * **Implementation Plan**:
            * Integrate with a vector database like Weaviate that supports hybrid vector/graph search, enabling more sophisticated reasoning over knowledge bases.
        * **Dependencies**: Vespa/Milvus alternative.
        * **Effort Estimate**: 2 weeks; Tests: Query accuracy.
        * **Metrics**: Retrieval precision >90%.

    * **User Story/Issue #902: Implement Dynamic Knowledge Graphs via Graphiti**
        * **Status**: Not Started
        * **Goal**: Temporal evolving memory.
        * **AC**: Graphiti for relational capture.
        * **Implementation Plan**:
            * Explore using Graphiti to give agents a temporal, evolving memory that captures not just facts, but the relationships between them.
        * **Dependencies**: Neo4j alternative for scalability.
        * **Effort Estimate**: 2 weeks; Tests: Graph evolution sims.
        * **Metrics**: Relationship recall >85%.

## **3.0 Appendix**

### **3.1. Tooling Cheatsheet**

**Core Tools**:

* **MCP/JSON-RPC**: Protocol setup—mcp-client install for AI comms.
* **GraalVM**: Bindings—graalvm-ce install for polyglot.
* **Firecracker/Podman**: Sandbox—podman run --rm for tests.
* **MLflow/Neptune.ai**: PLM—mlflow ui for tracking.
* **CrewAI/LangGraph**: HITL—crewai init for agents.
* **Semgrep/Guardrails AI**: Security—semgrep --config=auto scans.
* **Airtable**: Prioritization—API for RICE/MoSCoW scoring.
* **Deepgram/AssemblyAI**: Voice—deepgram transcribe for ideation.
* **Lunary/Phoenix**: Observability—lunary dashboard for traces.

**Dev Commands**:

* Build Core: cargo build --release.
* Test Sandbox: firecracker --api-sock /tmp/frame.sock.
* Deploy n8n: docker-compose up -d.

### **3.2. Contribution Guidelines**

*(See CONTRIBUTING.md for full details; summary: Fork repo, branch as feature/\[name\]; PRs with tests/docs; follow CODE_OF_CONDUCT.md. Use issues for bugs/features; discuss in GitHub Discussions. All contributions under MIT license.)*

### **3.3. Change Log**

* **v1.2.0 (2025-07-22)**: Incorporated alternatives (e.g., Lunary for observability, Deepgram for voice); added estimates/metrics/risks; populated appendix. Initial release of brief.
* **v1.1.0 (2025-07-15)**: Added governance epics; refined priorities based on trends.
* **v1.0.0 (2025-07-01)**: Initial vision and roadmap synthesis.
